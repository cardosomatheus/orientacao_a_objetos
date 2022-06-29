class Gato:
    tipo_animal = 'Felino'

    def __init__(self, nome):
        self.nome = nome


cat1 = Gato('jhon')
cat2 = Gato('kiki')
cat1.tipo_animal = 'Bichano'

print(cat1.tipo_animal)
print(cat2.tipo_animal)
print('-'*10)

print(cat1.nome)
print(cat2.nome)
