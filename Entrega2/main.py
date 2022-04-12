# Here we are going to work in the web scrapper and the NPL data

from unittest import result
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
import requests
import re

url = "https://www.bbc.com/mundo"  # url of the page to be scraped

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# print(doc)

# obtain the title of each article

tag = doc.find(["ul"],  class_="e57qer20 bbc-10m7ymo eom0ln50")
# Name of the article
tag2 = tag.find_all(["a"], class_="bbc-1fxtbkn evnt13t0")
# time of the article
tag3 = tag.find_all(["time"], class_="bbc-2y0240 e4zesg50")

'''print(tag2[0].contents)

a = tag2[0].contents        # Name of the article

print(a[0].text)'''

'''print(tag3[0])

b = tag3[0]            # Time of the article 

print(b['datetime'])'''
