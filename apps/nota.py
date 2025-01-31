from apps.operator import Operator


class Nota:
    _nota1 = 0
    _nota2 = 0

    # Constructor
    def __init__(self, nota1, nota2):
        self._nota1 = nota1
        self._nota2 = nota2
        self.operator = Operator

    @property
    def nota1(self):
        return self._nota1

    @property
    def nota2(self):
        return self._nota2

    @nota1.setter
    def nota1(self, nota1):
        self._nota1 = nota1

    @nota2.setter
    def nota2(self, nota2):
        self._nota2 = nota2

    def nota_total(self):
        return self.operator.soma(self._nota1, self._nota2)
