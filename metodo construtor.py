class Gato:
    """ Classe com foco no felino Gato"""

    def __init__(self, nome):
        """ capturando o nome do gato"""
        self.nome = nome
        print('seu gatinho se chama: ', self.nome)

    def peso_gato(self, peso):
        """ Capturando o peso do gato"""
        self.peso = peso

        if self.peso > 5.0:
            print('seu gato está gordinho.')
        elif self.peso > 3.5:
            print('peso parece normal.')
        else:
            print('gatinho abaixo do peso.')

    def _dieta_especial_gato(self):
        """ Descobrindo a recomendação do felino"""
        self.msg = 'Tudo ok'

        if peso < 3.5:
            self.msg = 'Aumente a ração do felino, ele esta muito magrinho.'
        elif peso >= 5.0:
            self.msg = 'Diminua a ração do felino, ele está gordinho.'
        return self.msg

    def dados_gato(self):
        print(f'\n O gato {self.nome} está com {self.peso}kg')
        print(self._dieta_especial_gato())


nome_gato = str(input('O NOME DO SEU GATO: '))
cat = Gato(nome_gato)

peso = float(input('QUAL O PESO DO SEU GATO EM KG: '))
cat.peso_gato(peso)

cat.dados_gato()
