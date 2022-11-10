import pdfplumber
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import os
import timeit
import psutil
import string
import re

start = timeit.default_timer()
file_path = 'Ley de Bioseguridad de Organismos Geneticamente Modificados.pdf'
pdf = pdfplumber.open(file_path)

with open('Ley de Bioseguridad de Organismos Geneticamente Modificados.txt', 'w') as f:
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

filename = "Ley de Bioseguridad de Organismos Geneticamente Modificados.txt"
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

end = timeit.default_timer()
print('Tiempo total de ejecucion: ', end - start)
print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)