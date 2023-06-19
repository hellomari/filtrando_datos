#Definición de lista

Lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

#creación de unción 
def hacer_grandioso(lista):
    for i in range(len(lista)):
        if lista[i] in ["Harry Houdini", "David Blaine", "Teller"]:
            lista[i] = "El gran " + lista[i]

            #basicamente crea por cada elemento " el gran" esto gracias a len
            #q cuenta cuantos elementos hay en la lista
            #

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

        #por cada nombre de la lista


magos = []
cientificos = []
otros = []

for nombre in Lista:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

print("Nombres de los magos:")
imprimir_nombres(magos)
print()

print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()

print("Nombres restantes:")
imprimir_nombres(otros)

print("Lista completa de nombres:")
imprimir_nombres(Lista)
print()
