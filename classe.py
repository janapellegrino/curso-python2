class Dog():
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.fome = 0
    
    def andar(self):
        self.fome += 1
        return 'Andando... fome:{}'.format(self.fome)
    
    def comer(self):
        self.fome -= 1
        return 'Comendo... fome:{}'.format(self.fome)

dog1 = Dog('bilu', 4, 'pitbull')

print(dog1.fome)
dog1.andar()
dog1.andar()
dog1.andar()
dog1.comer()
print(dog1.fome)