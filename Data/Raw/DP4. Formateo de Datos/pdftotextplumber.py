import pdfplumber
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import os
import timeit
import psutil
import string
import re

start = timeit.timeit()
file_path = 'LeyGeneraldelEquilibrioEcologicoylaProteccionalAmbiente.pdf'
pdf = pdfplumber.open(file_path)

with open('text.txt', 'w') as f:
    for page_num in pdf.pages:
        # print('Page: {0}'.format(page_num))
        #pageObj = pdf.pages[0]
        
        try:
            txt = page_num.extract_text()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()

filename = "text.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "El archivo " + filename + " no existe"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("El archivo " + filename + " contiene: " + str(num_words) + " palabras")
    
#####------------------Proceso de eliminaci�n de ruido ---------------------------
file = open('text.txt', 'r')

text = file.read()
# convirtiendo en palabras
tokens = word_tokenize(text)
# eliminar todos los tokens que no est�n en orden alfab�tico
words = [word for word in tokens if word.isalpha()]
print(words)

from nltk.corpus import stopwords
stop_words = stopwords.words('spanish')
#print(stop_words)
['a', 'ac�', 'ah�', 'al', 'algo', 'alg�n/a/o/s', 'all�/�', 'ambos', 'ante', 'antes', 'aquel', 'aquella/o/s', 'aqu�', 'arriba', 'as�', 'atr�s', 'aun', 'aunque', 'bien', 'cada', 'casi', 'como', 'con', 'cual', 'y', 'sobre', 'los', 'en', 'la', 'de', 'yo']

#Se crea el archivo txt cargado del texto filtrado
file = open("filter_text.txt", "w")
file.write(str(words))
file.close()

#Conteo de palabras ya filtradas
filename2 = 'filter_text.txt'

try:
    with open(filename2) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "El archivo " + filename2 + " no existe"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("El archivo " + filename2 + " contiene: " + str(num_words) + " palabras")

end = timeit.timeit()
print('Tiempo de ejecucion: ', end - start)
print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)