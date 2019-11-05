from googlesearch import search_news


query_string = 'Кива'

result = search_news(query_string, stop=None, pause=5.0, tbs="qdr:m")

# for article in result:
# 	print(article)

print(len(list(result)))
