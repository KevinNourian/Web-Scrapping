###############################
## Web Scrapping
## http://quotes.toscrape.com/
###############################

import requests
import bs4

## Web Scrapping
## Task 1
## Get the names of authors from the first page of the site.

result = requests.get(" http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text, 'lxml')

authors = set()
for name in soup.select('.author'):
    authors.add(name.text)

print('Authors from Page 1:')
print(authors)
print()


## Web Scrapping
## Task 2
##  Create a list of all the quotes from the first page of the site.

print('Quotes from Page 1:')
for item in soup.select('.text'):
    print(item.text)
print()


## Web Scrapping
## Task 3
## Create a list of the names of the top 10 tags from the first page of the site.

tags = []

for item in soup.select(".tag-item"):
    tags.append(item.text)

print('Tags from Page 1:')
print(tags)
print()


## Web Scrapping
## Task 4
## Get the names of unique authors from the entire website.

base_url = 'http://quotes.toscrape.com/page/{}/'

found = False
page = 2
authors = set()

while found == False:
    scrape_url = base_url.format(page)
    result = requests.get(scrape_url)
    result.text
    if 'No quotes found!' in result.text: # We know that 'No quotes found!' is on all invalid pages.
        found = True
    else:
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        for item in soup.select('small'):
            authors.add(item.text)

    page += 1

print('Authors from the entire site:')
print(authors)
