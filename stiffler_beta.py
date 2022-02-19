import time
import requests
from bs4 import BeautifulSoup as bs
import lxml

#url = 'https://www.apple.com/fr/newsroom/'
url = 'https://www.ssi.gouv.fr/actualites/'
response = requests.get(url)
text = response.text
soup = bs(text, 'lxml')


#Get all articles titles
date_tag = soup.find_all('p', {'class': 'date'})
li_tag = soup.find_all("h3")

articles = []
title = []
text = []
date = []
compt = 0

#put titles in list
for article in li_tag:
    articles.append(article.string)


#put dates
for elem in date_tag:
    elem.name = "p_date"
    date.append(elem.string)

p_tag = soup.find_all('p')
for p in p_tag:
    if p.has_attr('id'):
        continue
    text.append(p.string)

if len(text) == len(date) and len(date) == len(articles):
    print("Les tableux ont la meme taille !\n")
    while len(text) != compt:
        print(articles[compt])
        print(date[compt])
        print(text[compt])
        print("\n\n")
        compt += 1
else :
    print("title:" + str(len(title)))
    print("date:" + str(len(date)))
    print("text:" + str(len(text)))

print(compt)
