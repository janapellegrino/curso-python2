#read() ler arquivo inteiro
#readline ler linha do arquivo
#readlines ler arquivo inteiro com linha


# arquivo = open('frutas.txt', 'r')

# for x in arquivo.readlines():
#     print(x.replace('\n', ''))


# with open('frutas.txt', 'a+') as arquivo:
#     for x in arquivo.readlines():
#         print(x.replace('\n', ''))

# #adicionar uma fruta no arquivo (muito legal!!)
# with open('frutas.txt', 'a+') as arquivo:
#     fruta = input('Digite a fruta: ')
#     arquivo.write(fruta + '\n')

#     with open('frutas.txt', 'r') as arquivo:
#         print(arquivo.read())

#separa por palavra uma frase
#texto.split()




arquivo = open('cidades.txt', 'w')
while True:
    cidades = input('Digite o nome de uma cidade: ')
    if cidades.lower() == 'sair':
        break
    arquivo.write(cidades + '\n')