
# try:
from jupiter.sentient.aspect.reviewProcessing import ReviewP
from jupiter.sentient.aspect.sentimental import Sentiment
from jupiter.sentient.aspect.aspectratings import AspectR


from jupiter.sentient.reviews.nlp import WordCloud
<<<<<<< HEAD
from jupiter.sentient.reviews.holidaypool import HolidayIQ
from jupiter.sentient.reviews.bookingpool import Booking
=======
>>>>>>> d67bd6ed19345d19064aebff4a681546f8ded5d3



# except:
# 	from aspect.reviewProcessing import ReviewP
# 	from aspect.sentimental import Sentiment
# 	from aspect.aspectratings import AspectR
# 	from reviews.trippool import TripAdvisor
# 	from reviews.zomatopool import Zomato
# 	from reviews.nlp import WordCloud
verbose= True
class Sentient(object):
	"""docstring for Sentient"""
	def __init__(self,url,survey_id,provider,aspect_notation):
		self.u=url
		self.sid= survey_id
		self.p= provider
		self.aspect_notation=aspect_notation
	def scrap_data(self):
		print(self.aspect_notation)
		if "zomato.com" in self.u:
			from jupiter.sentient.reviews.zomatopool import Zomato
			Zomato(self.u,self.sid).get_data()
		if "tripadvisor" in self.u:
			from jupiter.sentient.reviews.trippool import TripAdvisor
			TripAdvisor(self.u,self.sid).get_data()
		if "holidayiq" in self.u:
			from jupiter.sentient.reviews.holidaypool import HolidayIQ
			HolidayIQ(self.u,self.sid).get_data()
		if "booking.com" in self.u:
			from jupiter.sentient.reviews.bookingpool import Booking
			Booking(self.u,self.sid).get_data()

	def wordcloud(self):
		WordCloud(self.sid,self.p).wc()
	def run_ml(self):

		ReviewP(self.sid,self.p,self.aspect_notation).run()
		print("ReviewP Done")

		Sentiment(self.sid,self.p).run()
		print("Sentiment Done")

		AspectR(self.sid,self.p).run()
		print ("AspectR Done")

	def run(self):
		if verbose:print ("Starting Scraping")
		self.scrap_data()
		if verbose:print("Starting WordCloud")
		self.wordcloud()
		if verbose: print("Running ML")
		self.run_ml()
		print("Done")
if __name__ == '__main__':
	# url= "https://www.zomato.com/ncr/purani-dilli-restaurant-zakir-nagar-new-delhi"
	url="http://www.booking.com/hotel/in/swissa-tel-goa.html?label=gen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmaGyIAQGYATG4AQ_IAQ_YAQHoAQH4AQKoAgM;sid=69a80e530b4bd33d6a2ce0e128061485;dcid=12;dest_id=4127;dest_type=region;dist=0;group_adults=2;room1=A%2CA;sb_price_type=total;srfid=39183e2a96da4c1e9df94a8b1555fa36ec6494ddX4;type=total;ucfs=1&"
	survey_id="vOAWLlOmAZyY23AdmZy"
	provider="booking"
<<<<<<< HEAD
	Sentient(url,survey_id,provider,["ambience","value_for_money","room_service","cleanliness","amenities"]).run()

=======
	Sentient(url,survey_id,provider,["ambience","value_for_money","room_service","cleanliness","amenities"]).run()
>>>>>>> d67bd6ed19345d19064aebff4a681546f8ded5d3
