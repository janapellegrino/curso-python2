from datetime import datetime

try:
    while True:
        number = int(input('Digite um numero inteiro: '))
        if number == 0:
            break
except ValueError as e:
    with open('python.log', 'a') as arquivo:
        arquivo.write('{} {}\n'.format(e, datetime.now()))
except KeyboardInterrupt as e:
    print('pra que iniciou!')
    with open('python.log', 'a') as arquivo:
        arquivo.write('{} {}\n'.format(e, datetime.now()))

finally:
    print('programa finalizado')