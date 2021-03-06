class Teste:
    """ Conceito de encapsulamento de objetos
        Método Getter = recupera valores armazenados no objeto
        Método Setter = altera o valor da variavel"""
    def __init__(self, valor):
        self.x = valor

    def get_valor(self):
        """ Método getter com o return do atributo x"""
        return self.x

    def set_valor(self, v):
        """ Método setter para atribuir um novo valor ao atributo x"""
        self.x = v


teste = Teste(10)
print(f'valor de objeto:  {teste.get_valor()}')     #leitura do valor na variavel
print('-'*10)

valor = int(input('Digite um valor numerico: '))
teste.set_valor(valor)  # Alteração do valor da variavel
print(f'valor de objeto após a atribuição setter:  {teste.get_valor()}')

