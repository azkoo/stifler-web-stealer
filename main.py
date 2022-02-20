from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import lxml
import functions as f
import stiffler_beta as stiff

#GET URL and his content
#url = 'https://www.apple.com/fr/newsroom/'
url = 'https://www.ssi.gouv.fr/actualites/'
response = requests.get(url)
text = response.text
soup = bs(text, 'lxml')


#SOUP COMMANDS
#get all p tag with class = 'date'
date_tag = soup.find_all('p', {'class': 'date'})
#get all h3 tags
li_tag = soup.find_all("h3")

stiff.get_titles(li_tag)
stiff.get_dates(date_tag)

p_tag = soup.find_all('p')
stiff.get_texts(p_tag)

stiff.print_articles()

