# Here we are going to work in the web scrapper and the NPL data

from nltk.tokenize import word_tokenize
from regex import P
from sympy import N
from bs4 import BeautifulSoup
import numpy as np
import requests
import pandas as pd
import re
import nltk
import matplotlib.pyplot as ptl
import csv
from os import path
from PIL import Image
import random
nltk.download('punkt')


# Se obtiene la lista de stopwords mediante la libreria nltk
stopW = ['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad',
         'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía', 'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened']


url = "https://www.bbc.com/mundo"  # url of the page to be scraped

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

title = []
date = []
summary = []

data = []


# obtain the title of each article


tag5 = doc.find_all(["div"], class_="bbc-1sk5sm2 e19k1v2h0")

print(tag5[0])
print("\n")


for i in range(31):

    print(i)
    print("\n")
    temp = tag5[i].find(["a"], class_="bbc-1fxtbkn evnt13t0")
    tempa = temp.span.string
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


dict = {'title': title, 'date': date, 'summary': summary}
df = pd.DataFrame(dict)

# saving the dataframe          #pandas
df.to_csv('GFG.csv', index=False, encoding='utf-8-sig', header=True, sep=',')


def plot(a, b):
    ptl.bar(a, b)
    ptl.xticks(rotation=90)
    ptl.show()


def clean_text(text):
    clean = []
    array_clean = []
    tempW = []
    tempW2 = []
    patron = re.compile(r"(\w+)")

    for k in range(len(text)):
        st = str(text[k])
        m = patron.findall(st)
        array_clean.append(m)

    for i in range(len(array_clean)):
        tempW2 = []
        if array_clean[i] != None:
            #tempW = array_clean[i].split()
            tempW = array_clean[i]
            for j in range(len(tempW)):
                if tempW[j] not in stopW:
                    tempW2.insert(j, tempW[j])
            clean.append(tempW2)
        else:
            continue

    return clean


# 1
def distribution_Frequency(lits):
    freq = {}
    F = []
    key_list = []
    patron = re.compile(r"(\w+)")
    for i in range(len(lits)):
        st = str(lits[i])
        m = patron.findall(st)
        for palabra in m:
            palabra = palabra.lower()
            if palabra in freq:
                freq[palabra] += 1
            else:
                freq[palabra] = 1
    key_list = list(freq.keys())
    F = list(freq.values())
    return key_list, F, freq


print(clean_text(title))
arr = clean_text(title)
arr2 = clean_text(summary)
complete_arr = arr + arr2


name, f, F = distribution_Frequency(arr)

'''ptl.bar(name, f)
ptl.xticks(rotation=90)
ptl.show()'''
plot(name, f)


# 2

def date_2(date, arr, arr2):

    freq = {}
    data = {}
    dates = list(set(date))
    patron = re.compile(r"(\w+)")
    # divide the array in two parts
    for j in range(len(dates)):
        for i in range(len(arr)):
            temp_title = str(arr[i])
            temp_summary = str(arr2[i])
            m = patron.findall(temp_title)
            m2 = patron.findall(temp_summary)
            array_m = m + m2
            temp_date = str(date[i])
            if temp_date == dates[j]:
                for word in array_m:
                    word = word.lower()
                    if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
        cont = cont = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        temp_cont = list(cont[-len(cont)])
        data[dates[j]] = temp_cont

    key_list = list(data.keys())
    item_list = list(data.items())

    return data, key_list, item_list


print("\n")
print("Segundo punto\n")
data, key_l, item_l = date_2(date, arr, arr2)
print(data)


# 3


def date_distribution(date):

    freq = {}
    for i in range(len(date)):
        st = str(date[i])
        if st in freq:
            freq[st] += 1
        else:
            freq[st] = 1
    return freq


print("\n")
print("\n")
print("Tercer punto\n")
print(date_distribution(date))


# 4
# CloudWord


def obtenNGramas(listaPalabras, n):
    return [listaPalabras[i:i+n] for i in range(len(listaPalabras)-(n-1))]


def lower(listaPalabras):
    arr = []
    temp_arr = []
    for i in range(len(listaPalabras)):
        words = listaPalabras[i]
        temp_arr = []
        for word in words:
            word = word.lower()
            temp_arr.append(word)
        arr.append(temp_arr)
    return arr


# 5


def bigramas(listaPalabras):
    print("\n")
    print("\n")
    print("\n")
    freq = {}
    bigramas = []
    temp_bi = []
    listaPalabras = lower(listaPalabras)

    for l in range(len(listaPalabras)):
        word_ = listaPalabras[l]
        temp_bigramas = obtenNGramas(word_, 2)
        for g in range(len(temp_bigramas)):
            bigramas.append(temp_bigramas[g])
            temp_bi.append(temp_bigramas[g])

    for i in range(len(bigramas)):
        word = temp_bi[i]

        word2 = str(word[0] + " " + word[1])
        if word in bigramas:

            if word2 in freq:

                freq[word2] += 1
            else:

                freq[word2] = 1

    cont = cont = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for j in range(10):
        print(cont[j])


def trigramas(listaPalabras):
    print("\n")
    print("\n")
    print("\n")
    freq = {}
    trigramas = []
    temp_tri = []
    listaPalabras = lower(listaPalabras)

    for l in range(len(listaPalabras)):
        word_ = listaPalabras[l]
        temp_trigramas = obtenNGramas(word_, 3)
        for g in range(len(temp_trigramas)):
            trigramas.append(temp_trigramas[g])
            temp_tri.append(temp_trigramas[g])

    for i in range(len(trigramas)):
        word = temp_tri[i]

        word2 = str(word[0] + " " + word[1] + " " + word[2])
        if word in trigramas:

            if word2 in freq:

                freq[word2] += 1
            else:

                freq[word2] = 1

    cont = cont = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for j in range(10):
        print(cont[j])


print("Quinto punto\n")
print("Los 10 bigramas mas frecuentes son:")
bigramas(complete_arr)
print("\n")
print("\n")
print("Los 10 trigramas mas frecuentes son:")
trigramas(complete_arr)


# 6


with open("file.txt", 'w', encoding='utf8') as file:
    for row in complete_arr:
        s = " ".join(map(str, row))
        file.write(s+'\n')
txt = open('file.txt', encoding='utf8').read()


def markov_chain(txt):

    corpus = txt.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = 50

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    text = ' '.join(chain)

    print(text)


print("\n")
print("\n")
print("Sexto Punto\n")
print("\n")
for i in range(30):
    print("\n")
    print("Noticia: ", i)
    print("\n")
    markov_chain(txt)
