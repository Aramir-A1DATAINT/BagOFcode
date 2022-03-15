# https://morioh.com/p/6953e112338e

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Web Scraping With Python and BeutifulSoup
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
## print(r.content) # contents 전부 print
# Create a BeautifulSoup object
# !pip install html5lib
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify()) # contents를 HTML화 시켜서 뽑아 냄
                       # html을 보기 좋게 만들어주는 패키지 .prettify

quotes=[]  # a list to store quotes
table = soup.find_all('div', attrs = {'class':'container'}) # find div elemet using find method

for row in soup.find_all('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quotes.append(quote)

data = pd.DataFrame(quotes)
print(data.head()) 

