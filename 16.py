lista = [5, 4, 3, 2, 1]
size = len(lista)

# for 1: garantir que vamos trocar o suficiente
# for 2: passar pela lista trocando os elementos
# se estiver fora de ordem => eu troco
# troco baseado no critério do if
for _ in range(size):
    for pos in range(0, size - 1):
        if lista[pos] > lista[pos + 1]:
            lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos]
print(lista)

#ordem descrescente
for _ in range(size):
    for pos in range(0, size - 1):
        if lista[pos] < lista[pos + 1]:
            lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos]
print(lista)
          
# trocando dois valores
#forma tradicional
a = 2
b = 3

aux = a
a = b
b = aux

# outra forma

a, b = b, a



