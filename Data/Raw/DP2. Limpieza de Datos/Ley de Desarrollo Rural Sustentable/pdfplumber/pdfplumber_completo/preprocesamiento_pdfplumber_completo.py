import pdfplumber
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import unidecode
import os
import timeit
import psutil
import string
import re

start = timeit.default_timer()
file_path = 'Ley de Desarrollo Rural Sustentable.pdf'
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
    
##--------------------------------------------------------------------------------

# creating a pdf file object
file = open('text.txt', 'r')

text = file.read()

#Tokenización
#La tokenización es el primer paso en el análisis de texto. 
#El proceso de dividir un párrafo de texto en fragmentos más pequeños, 
#como palabras o oraciones, se denomina tokenización. El token es una entidad 
#única que es un bloque de construcción para una oración o un párrafo.

from nltk.tokenize import sent_tokenize

#text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
#The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text=sent_tokenize(text)
print("Tokenize:", tokenized_text)


#---------------------------------------------------------------------


#Segmentación de palabras
#El Segmentador de palabras divide el párrafo de texto en palabras.

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print("Segmentation", tokenized_word)


#---------------------------------------------------------------------


#Stopwords
#Eliminación de ruido

#Palabras vacías consideradas como ruido en el texto. El texto puede contener 
#palabras vacías como is, am, are, this, a, an, the, etc.

#En NLTK para eliminar palabras vacías, debe crear una lista de palabras vacías y 
#filtrar su lista de tokens de estas palabras.


from nltk.corpus import stopwords
stop_words=set(stopwords.words("spanish"))
print(stop_words)

#Eliminar palabras vacías

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent)


#--------------------------------------------------------

#Normalización

#La normalización del léxico considera otro tipo de ruido en el texto. 
#Por ejemplo, conexión, conectado, palabra de conexión se reduce a una palabra 
#común "conectar". Reduce las formas derivadas de una palabra a una raíz común.

#Derivación
#Stemming es un proceso de normalización lingüística, que reduce las palabras a su 
#palabra raíz o elimina los afijos derivativos. Por ejemplo, conexión, conectado,
#palabra de conexión se reduce a una palabra común "conectar".


# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)

#remover acentos
for i in range(len(stemmed_words)):
    # remove ascents
    stemmed_words[i] = unidecode.unidecode(stemmed_words[i])

#Remover puntuaciones
punctuations="?:!.,;-)("
for word in stemmed_words:
    if word in punctuations:
        stemmed_words.remove(word)
print(" ")
print("Remove stopword & Punctuation")
print(stemmed_words)


#Se crea el archivo txt cargado del texto filtrado
file = open("filter_text.txt", "w")
file.write(str(stemmed_words))
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
    num_words2 = len(words)
    print("El archivo " + filename2 + " contiene: " + str(num_words2) + " palabras")
    
end = timeit.default_timer()
print('Tiempo total de ejecucion: ', end - start)
print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)