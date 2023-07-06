import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
url='https://economictimes.indiatimes.com/markets'
r=requests.get(url)
#print(r.text)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
news=soup.find_all('ul',class_='newsList')
comp=soup.find_all('div',class_='stry')
#print(a)
#list1=[]

for article in news:
  for title in article.find_all('a'):
    b=title.get_text()
    #list1.append(b)
    #print(b)
    
    obj=TextBlob(b)
    sentiment=obj.sentiment.polarity
    #print(sentiment)
    c=title.get('href')
    if(sentiment>=0.1):
      print(b+" "+"-"+" "+"https://economictimes.indiatimes.com"+c)




for art in comp:
  for title in art.find_all('a'):
    e=title.get_text()
    #print(e)
    obj1=TextBlob(e)
    sentiment1=obj1.sentiment.polarity
    f=title.get('href')
    if sentiment1>=0.1:
      print(e+" "+"-"+" "+"https://economictimes.indiatimes.com"+f)

'''for article in news:
  for link in article.find_all('a'):
    print(link.get('href'))'''



'''for h in href.find_all('href',href_=True):
      #d=h.get_text()
      print(h.get(href))
'''





'''obj=TextBlob(b)
    sentiment=obj.sentiment.polarity
    print(sentiment)'''


'''sentiment=b.sentiment.polarity
print(polarity)'''


'''df=pd.DataFrame(list1)
df.head()
#df.to_csv('scrape.csv')'''


'''
#print(a.children)
for a in a.children:
  
  d=a.get_text()
  list1.append(d)
  print(list1)
  print('\n')
exit()
print(a.get_text())

for i in a.children:
    print("child :  ", i)



b=a.find_all('title')
print(a.prettify())
print(b)
for b in b :
  c=b.find('title',class_='titleis')
  print(c.text.strip())
  
#print(soup)
print(soup.find('a'))
exit()
for title in a:
  print(title)'''




'''from textblob import TextBlob
from newspaper import Article
url='https://economictimes.indiatimes.com/markets'
article=Article(url)
article.download()
article.parse()
article.nlp()
text=article.summary
print(text)'''