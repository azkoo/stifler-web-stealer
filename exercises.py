import time
import requests
from bs4 import BeautifulSoup as bs
import lxml

#url = 'https://www.apple.com/fr/newsroom/'
url = 'https://www.ssi.gouv.fr/actualites/'
response = requests.get(url)
text = response.text
soup = bs(text, 'lxml')

#links = soup.find_all("a")
#for link in links:
#    if "france.fr" in link.text:
#        print(link)
#        print(link.attrs['href'])
#        print(link.text)

#articles = data.find_all(role = "list")
#for article in articles:
#    print(article)
#    #news = soup.get_text()