import pdfplumber
import timeit
import psutil

start = timeit.default_timer()
start1 = timeit.default_timer()
file_path = 'Ley General de Vida Silvestre.pdf'
pdf = pdfplumber.open(file_path)

with open('Ley General de Vida Silvestre.txt', 'w') as f:
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
end1 = timeit.default_timer()

start2 = timeit.default_timer()
filename = "Ley General de Vida Silvestre.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "El archivo " + filename + " no existe"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    
end2 = timeit.default_timer()
end = timeit.default_timer()

print("El archivo " + filename + " contiene: " + str(num_words) + " palabras")

# print('Tiempo 1: ', start1)
# print('Tiempo END 1: ', end1)
# print('Tiempo 2: ', start2)
# print('Tiempo END 2: ', end2)
t1=end1 - start1
t2=end2 - start2
print('Tiempo de pdf a txt: ', t1)
print('Tiempo de contador de palabras: ', t2)
print('Tiempo total', t1+t2)
print('Tiempo total de ejecucion: ', end - start)
print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)