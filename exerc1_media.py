#!/usr/bin/python3
nome = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
falta = int(input('Digite a quantidade de faltas: '))
media = (nota1 + nota2) / 2

if media >= 7 and falta <= 4:
    resultado = 'aprovado'
else:
    resultado = 'reprovado!'

print('o aluno {} teve a media de {} e foi {}'.format (nome, media, resultado))