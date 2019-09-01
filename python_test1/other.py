
'''
     Maestria tiene Ediciones, coordinador, comité académico (se guarda cuando se actualiza)
    Maetria tiene el expediente del programa, el expediente de cada edicion
    Ediciones tiene Grupos
    Ediciones tiene Claustro (profesores y tutores), estudiantes, cursos
    profesores se guarda unos cuantos datos como por ejemplo el grado científico, categoría científica
    Una Edicion tiene un expediente
    Cada estudiante tiene un expediente

    Edicones tiene varios documentos importantes como son:
        - Carta de autorizo de inicio de edicion
        - Documento de lanzamiento de convocatoria
        - 
    Grupos tienen estudiantes


    Maestria tiene evaluaciones (Exelencia, Certificada, Avalada, Autorizada)

'''
nums = [55, 44, 33, 22, 11, 5, 1]

greater_than_five = [ i for i in nums if i > 5]

even = [i for i in nums if i%2 == 0]

even = list(filter(lambda x: x%2 == 0, nums))

#print(greater_than_five)
#print(even)

import winsound

i =0
while i < 10:
    winsound.PlaySound("*", winsound.SND_ALIAS)
    i+= 1

