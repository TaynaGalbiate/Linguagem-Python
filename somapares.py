lista1 = [2,11,3,6,4,17,10]
lista2 = [1,3,6,12,20,8]

#Exibir os números pares da lista 1 e 2
#Somar os números pares

def exibir_numeros_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

print("Números pares da lista 1: ")
exibir_numeros_pares(lista1)

print("Números pares da lista 2: ")
exibir_numeros_pares(lista2)

soma_pares = 0
for numero in lista1 :
    if numero % 2 == 0:
        soma_pares += numero

print("A soma dos números pares da lista 1 é: ", soma_pares)

soma_pares = 0
for numero in lista2 :
    if numero % 2 == 0:
        soma_pares += numero

print("A soma dos números pares da lista 2 é:", soma_pares)
