class Cubo:
    """    Classe de  calular o  cubo de um numero    """

    # dados da classe que serão compartilhados (atributos de classe)

    def __init__(self, valor):  # Metodo construtor da classe
        self.x = valor
        print('objeto criado!')

    def calcular_cubo(self):    # def para calcular o cubo
        cubo = self.x * self.x * self.x
        return 'cubo calculado:' + str(cubo)


teste = Cubo(500)
c = teste.calcular_cubo()
print(c)

