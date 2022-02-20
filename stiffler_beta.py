
####VARIABLES#

#lists creation
titles = []
texts = []
dates = []

#change a tag name
# second argument must be string
def change_tag_name(tag, new_name):
    tag.name = new_name

#put titles in a structured list
#content only
def get_titles(soup_request):
    for title in soup_request:
        titles.append(title.string)


#put dates in a structured list
#content only
def get_dates(soup_request):
    for date in soup_request:
        #date.name = "p_date"
        change_tag_name(date, "p_date")
        dates.append(date.string)

#p_tag = soup.find_all('p')
#put texts in a structured list
#content only
def get_texts(soup_request):
    for p in soup_request:
        if p.has_attr('id'):
            continue
        texts.append(p.string)

def print_articles():
    compt = 0
    if len(texts) == len(dates) and len(dates) == len(titles):
        print("Les tableux ont la meme taille !\n")
        while len(texts) != compt:
            print(titles[compt])
            print(dates[compt])
            print(texts[compt])
            print("\n\n")
            compt += 1
    else :
        print("title:" + str(len(titles)))
        print("date:" + str(len(dates)))
        print("text:" + str(len(texts)))








