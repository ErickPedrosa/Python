from random import choice
import collections

Carta = collections.namedtuple('Carta',['Valor', 'Naipe'])

class Copag:
    valor = [ str(n) for n in range(2, 11) ] + list('JQKA')
    naipe = "Espadas Ouros Paus Copas".split()
    
    def __init__(self):
        self._cartas = [Carta(valor, naipe) for naipe in self.naipe
                                            for valor in self.valor]
        
    def __len__(self):
        return len(self._cartas)
    
    def __getitem__(self, indice):
        return self._cartas[indice]
        
