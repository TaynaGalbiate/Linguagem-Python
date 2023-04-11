lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Mostrar os números da lista de 1 a 9
for x in range(1,10):
    print("Números de 1 a 9: " + str(lista[x]))
print("###############################")


#Mostrar os números de 8 a 13
for x in range (8,14):
    print("Números de 8 a 13: " + str(lista[x]))
print("###############################")

#Mostrar os números pares da lista
for x in lista:
    if(x % 2 == 0):
        print("Números pares: " + str(lista[x]))
print("###############################")

#Mostrar os números ímpares da lista
for x in lista:
    if(x % 2 != 0):
        print("Números ímpares: " + str(lista[x]))
print("###############################")

#Mostrar os múltiplos de 4
for x in lista:
    if (x % 4 == 0):
        print("Múltiplos de 4: " + str(lista[x]))
print("###############################")

#Mostrar descrescente
for x in range (15, -1, -1):
        print("Números decrescente: " + str (lista[x]))
print("###############################")
