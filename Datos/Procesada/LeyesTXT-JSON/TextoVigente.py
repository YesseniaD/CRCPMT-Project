import re
import os
import json
# filename = "Ley de Aguas Nacionales.txt"

# path_files = os.getcwd()
path_files = 'C://Users//YESS//Downloads//LEYESTXT-JSON'
file_list = os.listdir(path_files)

file_content = []

for filename in file_list:
    if os.path.isfile(filename):
        if filename != 'TextoVigente.py':
            with open(filename) as f_obj:
                contents = f_obj.read()
                file_content.append(contents)
                # print('ARCHIVO: ', filename)
                # print(contents)

                pattern_encabezado =  re.compile(r'\-{100} \nLEY.* \n \nC.MARA DE DIPUTADOS DEL H. CONGRESO DE LA UNI.N  \w+. \w+. DOF \d\d\-\d\d\-\d\d\d\d \nSecretar.a General \nSecretar.a de Servicios Parlamentarios')

                # pattern_pie_pagina = re.compile(r'^\d.* de \d.*')

                # matches = pattern.finditer(contents)
                matches = pattern_encabezado.findall(contents)

                # for match in matches:
                #     print(match)

                headers = matches[0]

                encabezado_str = {'ARCHIVO':filename, 
                                  'ENCABEZADO':headers}
                
                encabezado_json = json.dumps(encabezado_str, sort_keys=True, indent=4 ) 
                print(encabezado_json)


                # print('El encabezado es:\n\n')
                # print(matches[0])

                print(f'\n\nNumero de encabezados encontrados: {len(matches)}\n\n')
                


print('Numero de archivos es: ', len(file_content))




# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "El archivo " + filename + " no existe"
#     print(msg)
# else:
#     pattern_encabezado =  re.compile(r'\-{100} \nLEY.* \n \nC.MARA DE DIPUTADOS DEL H. CONGRESO DE LA UNI.N  \w+. \w+. DOF \d\d\-\d\d\-\d\d\d\d \nSecretar.a General \nSecretar.a de Servicios Parlamentarios')

#     # pattern_pie_pagina = re.compile(r'^\d.* de \d.*')

#     # matches = pattern.finditer(contents)
#     matches = pattern_encabezado.findall(contents)


#     for match in matches:
#         print(match)