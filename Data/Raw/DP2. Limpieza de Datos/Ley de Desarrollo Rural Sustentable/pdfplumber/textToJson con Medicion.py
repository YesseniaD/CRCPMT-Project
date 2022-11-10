import json
import timeit
import psutil

start = timeit.default_timer()
filename = 'Ley de Desarrollo Rural Sustentable.txt'
  
my_list = []

dict1 = {}
  
with open(filename) as fh:
  
    for line in fh:
  
        description = line.split()
  
        my_list.append(description)
        


def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

list_array = flatten(my_list)

out_file = open("Ley de Desarrollo Rural Sustentable.json", "w")
json.dump(list_array, out_file)
out_file.close()

end = timeit.default_timer()
print('Tiempo total de ejecucion: ', end - start)
print('Memoria RAM del Proceso: ', psutil.virtual_memory()[2])
print('Memoria RAM TOTAL: ', psutil.virtual_memory().total)