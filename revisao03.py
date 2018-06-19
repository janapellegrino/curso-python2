# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))
# nota4 = float(input('Digite a quarta nota: '))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print('A media das notas do aluno é {:3.2f}'.format(media))

#----------

soma = 0
for x in range(4):
    nota= float(input('Digite a nota {}: '.format(x+1)))
    soma += nota
print('A media é igual a {:.2f}'.format(soma/4))