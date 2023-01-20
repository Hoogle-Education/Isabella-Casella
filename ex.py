#Statistiques. Créer une liste qui contient les chiffres 2, 5, 8, 9, et 4. Réaliser un script qui permet d’afficher les éléments et de calculer la moyenne, le minimum, le maximum, la variance et l’écart-type.

lista = [2, 5, 8, 9, 4]
print(lista)

tamanho_lista = len(lista)
soma = 0

for numero in (lista):
    soma = soma + numero

#moyenne

moyenne = soma / tamanho_lista
print("Moyenne cest", moyenne)

#le minumun

suposto_menor = lista[0]
for numero in lista:
    if numero < suposto_menor:
        suposto_menor = numero

print("le minimum cest: ", suposto_menor)

#le maximum

suposto_maior = lista[0]
for numero in lista:
    if numero > suposto_maior:
        suposto_maior = numero

print("le maximun cest: ", suposto_maior)

#le maximum
# somatorio ((numero - media) **2 ) / n

variancia = 0

for numero in lista:
    variancia = variancia + (numero - moyenne)**2

variancia = variancia / tamanho_lista
# desvio_formatado = ':.2f'.format(variancia)
print('variancia é', '{:.2f}'.format(variancia))
# print(f'variancia é {variancia:.2f}')

desvio = variancia**2
print(desvio)
