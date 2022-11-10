from PyPDF2 import PdfFileReader, PdfFileWriter
import timeit
import psutil
    
start = timeit.default_timer()
file_path = '.\Ley General de Cambio Climatico.pdf'
pdf = PdfFileReader(file_path)

with open('Ley General de Cambio Climatico.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        # print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)
        
        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()
    
filename = "Ley General de Cambio Climatico.txt"
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