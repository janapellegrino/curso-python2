pessoas   = ['Jana', 'Solange', 'Marco']
pessoas[2] = 'Joao'

pessoas.append('Gabriela')
pessoas.insert(0, 'Boss')

for pessoa in pessoas:
    print('Ola {}, bem vindo!'.format(pessoa.title()))
    print('-----------')

while len(pessoas) > 0:
    pessoas.pop()
    print(pessoas)