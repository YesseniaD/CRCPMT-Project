import pdfplumber
import os
import timeit
import psutil
import string
import re
import csv

start = timeit.default_timer()
# file_path = 'Ley General del Equilibrio Ecologico y la Proteccion al Ambiente.pdf'
# file_path = 'Ley de Aguas Nacionales.pdf'
# file_path = 'Ley de Desarrollo Rural Sustentable.pdf'
# file_path = 'Ley General de Pesca y Acuacultura Sustentable.pdf'
# file_path = 'Ley General de Vida Silvestre.pdf'
# file_path = 'Ley General de Desarrollo Forestal Sustentable.pdf'
# file_path = 'Ley General Para la Prevención y Gestión Integral de Residuos.pdf'
# file_path = 'Ley Federal de Bioseguridad de Organismos Genéticamente Modificados.pdf'
# file_path = 'Ley General De Cambio Climático.pdf'

# Funcion open_file que realiza el proceso de conversion de pdf a text y separacion de palabras
def open_file(file_path):
    file_name = os.path.basename(file_path)
    pdf = pdfplumber.open(file_path)
    
    with open('text_pdfplumber.txt', 'w') as f:
        for page_num in pdf.pages:
            # print('Page: {0}'.format(page_num))
            #pageObj = pdf.pages[0]
            num_paginas = page_num
            try:
                txt = page_num.extract_text()
                # print(''.center(100, '-'))
            except:
                pass
            else:
                # f.write(''.center(100, '-'))
                f.write(txt)
        f.close()
    
    filename = "text_pdfplumber.txt"
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
    
    #Obtiene las palabras y las veces que se repiten en el archivo de texto
    copy_words=words
    frecuenciaPalab = [copy_words.count(w) for w in copy_words]
    new_lista=str(list(zip(copy_words, frecuenciaPalab)))
    
    
    end = timeit.default_timer()
    total_time= end - start
    # print (os.path.splitext(string">"file_path")[0])

#  Fuente: https://www.iteramos.com/pregunta/5172/como-obtener-el-nombre-del-archivo-sin-la-extension-de-una-ruta-en-python
    print('Nombre del archivo: ', file_path)
    print('Numero de paginas: ', num_paginas)
    print('Numero de paginas: ', num_words)
    print('Tiempo de ejecucion: ', end - start)
    print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
    print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)
    
    # Ciclo que lee cada palabra y la frecuencia y lo escribe en el csv
    for elemento in new_lista.split(')'):
        line_fi = file_name + " " + str(num_paginas) + " " + str(num_words) + " " + str(total_time) + " " + str(psutil.virtual_memory()[2]) + " " + str(psutil.virtual_memory().total) + str(elemento)
        with open('leyconpdfplumber.csv', 'a+') as f2:
            wr = csv.writer(f2)
            wr.writerow(line_fi.split(' '))


############## Termina la funcion open_file() 
# Aqui empieza a ejecutarse el programa

# crea archivo csv y agrega encabezado
with open('leyconpdfplumber.csv', 'w', newline='') as headercsv:
    writer = csv.DictWriter(headercsv, fieldnames = ["filename", "page_number", "num_words", "total time", "memoryporcent", "memorytotal", "word", "frecuencia"])
    writer.writeheader()


d = r"C:\Users\YESS\Downloads\Proyecto Mineria\Leyes"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        open_file(full_path)