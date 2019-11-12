from apiclient.discovery import build
import datetime


# Custom Search JSON API
api_key = 'AIzaSyDVCG3CoJJfkmbWVQ5WQDAyC_HegpGyFNw'
cx_id = '009517772569711013509:gbkpasmy6w6'



def total_search_results(search_query):
    """Return number of google searches for query from last month"""

    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    result = resource.list(q=search_query, cx=cx_id, sort=last_month_range()).execute()
    return result['searchInformation']['totalResults']


def last_month_range():
    today = datetime.date.today()
    today_string = today.strftime("%Y%m%d")
    last_month = today - datetime.timedelta(days=30)
    last_month_string = last_month.strftime("%Y%m%d")
    return f'date:r:{last_month_string}:{today_string}'
