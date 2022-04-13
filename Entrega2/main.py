# Here we are going to work in the web scrapper and the NPL data

from dataclasses import fields
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
import numpy as np
import requests
import pandas as pd
import csv
import re

url = "https://www.bbc.com/mundo"  # url of the page to be scraped

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

title = []
date = []
summary = []

data = []
fields = ["title", "date", "summary"]

# print(doc)

# obtain the title of each article


tag5 = doc.find_all(["div"], class_="bbc-1sk5sm2 e19k1v2h0")

print(tag5[0])
print("\n")


for i in range(31):
    # print(tag5[i])
    print(i)
    print("\n")
    temp = tag5[i].find(["a"], class_="bbc-1fxtbkn evnt13t0")
    '''tempa = temp.contents
    '''
    tempa = temp.span.string
    # print(tempa[0].text)
    title.append(tempa)
    print(tempa)
    print("\n")
    temp2 = tag5[i].find(["time"], class_="bbc-2y0240 e4zesg50")
    temp2a = temp2['datetime']
    date.append(temp2a)
    print(temp2a)
    print("\n")
    temp3 = tag5[i].find(["p"], class_="bbc-166eyoy e1tfxkuo1")
    temp3a = temp3.text
    summary.append(temp3.string)
    print(temp3a)
    print("\n")

    data1 = tempa
    data2 = temp2a
    data3 = temp3.string
    data.append([tempa, temp2a, temp3.string])


'''dict = {'title': title, 'date': date, 'summary': summary}
df = pd.DataFrame(dict)

# saving the dataframe          #pandas
df.to_csv('GFG.csv')

'''


'''with open('GFG', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
                                            # csv 
    write.writerow(fields)
    write.writerows(data)'''


"""np.savetxt("GFG.csv", 
           data,
           delimiter =", ",    #numpy 
           fmt ='% s')"""
