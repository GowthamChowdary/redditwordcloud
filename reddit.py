import requests
from wordcloud import WordCloud,STOPWORDS
url='https://api.pushshift.io/reddit/search/comment/?fields=body&limit=20000&link_id=e5vsuy'
# link_id will be available in the reddit url, just get the 6 char to drop it in here and get the word cloud for.
resp=requests.get(url)

data=resp.json()['data']
comments=" ".join(comment['body']for comment in data)
wc=WordCloud().generate(comments)
#print(comments) [was just testing, worked btw]

image = wc.to_file('img.png')

