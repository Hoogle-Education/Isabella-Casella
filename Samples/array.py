# numeros = input('digite uma sequencia: ')
# lista = numeros.split() # por padrão é o ' '(espaço)
# soma = 0

numeros = input('digite uma sequencia: ').split()
print(numeros)
soma = 0

for numero in numeros:
  soma += int(numero) # soma = soma + numero

print(soma)