class Cubo:
    """    Classe de  calular o  cubo de um numero    """

    # dados da classe que serão compartilhados (atributos de classe)

    def __init__(self, valor):  # Metodo construtor da classe
        self.x = valor
        print('objeto criado!')

    def calcular_cubo(self):    # def para calcular o cubo
        cubo = self.x * self.x * self.x
        return 'cubo calculado:' + str(cubo)


numero = int(input('Entre com um numero: '))
objcubo = Cubo(numero)  # instanciar  a classe

cubo = objcubo.calcular_cubo()
print(cubo)
