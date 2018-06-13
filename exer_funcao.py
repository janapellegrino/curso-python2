def ler_arquivo(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def escrever_arquivo(nome):
    with open(nome, 'a') as arquivo:
        conteudo = input('digite uma fruta: ')
        arquivo.write(conteudo + '\n')
    return True

def sobrescrever(nome):
    with open(nome, 'w') as arquivo:
        conteudo = input('Digite uma fruta: ')
        arquivo.write(conteudo + '\n')
    return True

escrever_arquivo('frutas.txt')
print(ler_arquivo('frutas.txt'))
