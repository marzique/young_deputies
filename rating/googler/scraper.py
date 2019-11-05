from googlesearch import search_news
import time
from datetime import timedelta

# doesnt work :(
def searches_by_deputy(query_string):
	result = search_news(query_string, stop=None, pause=10.0, tbs="qdr:m")
	return len(list(result))

# TODO: make google news scraper from scratch:
 # go to gs url with query, scroll unti possible.
 # count rows and return number
