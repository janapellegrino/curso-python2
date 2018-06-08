#!/usr/bin/python3
# letras =  ['a', 'b', 'c', ['d', 'e']]
# print(letras[3])

# numeros = [1, 2, 3, 4]

# for numeros in numeros:
#     print(numeros)

# numeros = list(range(10))

# for z in numeros:
#     if z % 2 == 0:
#         print(z)

# qtd = int(input('Digite um numero: '))

# for z in range(qtd):
#     if z % 2 == 0:
#         print(z)

pessoas = [
    {'nome': 'daniel', 'idade': 24},
    {'nome': 'rafael', 'idade': 6},
    {'nome': 'renata', 'idade': 23},
    {'nome': 'yasmin', 'idade': 4}

]

for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    print('O(A) {} tem {} anos'.format(nome, idade))
    print('-------------')