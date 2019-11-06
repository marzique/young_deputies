from apiclient.discovery import build


# Custom Search JSON API
api_key = 'AIzaSyDVCG3CoJJfkmbWVQ5WQDAyC_HegpGyFNw'
cx_id = '009517772569711013509:gbkpasmy6w6'


def total_search_results(search_query):
    """Return number of google searches for query from last month"""

    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    result = resource.list(q=search_query, cx=cx_id, dateRestrict='m1').execute()
    return result['searchInformation']['totalResults']
