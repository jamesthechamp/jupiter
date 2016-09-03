#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Survaider

"""Jupiter Task Runner - API endpoints.

This module provides interfaces to:
    - Add a task.
    - Get status.
    - Delete a task.
"""

from datetime import datetime as dt

import hug
import falcon
from mongoengine import ValidationError, NotUniqueError

from jupiter._config import version
from jupiter.api.directives import access_token
from jupiter.sentient.model import ZomatoQ, TripAdvisorQ


@hug.get('/{task_id}', versions=version)
def get_task(key: access_token, task_id: hug.types.text):
    pass

providers = {'zomato': ZomatoQ, 'tripadvisor': TripAdvisorQ}

def get_provider_class():
    pass

@hug.put('/', versions=version)
def put_task(key: access_token,
            provider: hug.types.one_of(list(providers.keys())),
            access_url: hug.types.text,
            survey_id: hug.types.text,
            children: hug.types.text,
            time_review: hug.types.text):
    provider_cls = providers[provider]
    time_rev = dt.striptime(time_review, "%Y-%m-%d")
    # I can write the logic below? Right.--NO
    aspects = aspects.split(",")

    if provider == "zomato":
        # Check if parent survey exists
        parent = ZomatoQ.objects(unique_identifier = survey_id+provider).count()
        try:
            if parent != 1:
                obj = ZomatoQ()
                obj.base_url = access_url
                obj.survey_id = survey_id
                obj.parent = "true"
                obj.unique_identifier = survey_id + provider
                obj.time_review = time_rev
                obj.save()
            obj2 = ZomatoQ()
            obj2.base_url = access_url
            obj2.survey_id = children
            obj2.parent_id = survey_id
            obj2.unique_identifier = children + provider
            obj.time_review = time_rev
            obj2.save()
            return obj2.repr
        except ValidationError:
            raise falcon.HTTPBadRequest(title='ValidationError',
                                        description='The parameters provided are invalid')
        except NotUniqueError:
            raise falcon.HTTPBadRequest(title='NotUniqueError',
                                        description='The given survey_id exists')
    elif provider == "tripadvisor":
        parent = TripAdvisorQ.objects(unique_identifier=survey_id+provider).count()
        try:
            if parent != 1:
                obj = TripAdvisorQ()
                obj.base_url = access_url
                obj.survey_id = survey_id
                obj.parent = "true"
                obj.unique_identifier = survey_id + provider
                obj.time_review = time_rev
                obj.save()
            obj2 = TripAdvisorQ()
            obj2.base_url = access_url
            obj2.survey_id = children
            obj2.parent_id = survey_id
            obj2.unique_identifier = children+provider
            obj2.time_review = time_rev
            obj2.save()
            return obj2.repr
        except ValidationError:
            raise falcon.HTTPBadRequest(
                title='ValidationError',
                description='The parameters provided are invalid')
        except NotUniqueError:
            raise falcon.HTTPBadRequest(
                title='NotUniqueError',
                description='The given survey_id exists')

@hug.delete('/{task_id}', versions=version)
def delete_task(key: access_token, task_id: hug.types.text):
    pass
