from apiclient.discovery import build


# Custom Search JSON API

# TODO: wrap this shit to a function
api_key = 'AIzaSyDVCG3CoJJfkmbWVQ5WQDAyC_HegpGyFNw'
url = 'https://www.googleapis.com/customsearch/v1?'
cx_id = '009517772569711013509:gbkpasmy6w6'
search_query = 'Константин Бондаренко'

resource = build('customsearch', 'v1', developerKey=api_key).cse()

result = resource.list(q=search_query, cx=cx_id, dateRestrict='m1').execute()

# needed int
total_results = result['searchInformation']['totalResults']
print(f'{search_query}: {total_results}')
