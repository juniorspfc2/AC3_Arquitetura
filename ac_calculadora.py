import abc



class Calculadora(object):
    def calcular(self,valor1,valor2,operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return "ERRO" 
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado



class OperacaoFabrica(object):
    def criar(self,operador):
        if operador == "Divisao":
            return Divisao()
        elif operador == "Soma":
            return Soma()
        elif operador == "Subtracao":
            return Subtracao()
        elif operador == "Multiplicacao":
            return Multiplicacao()

 


class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self,valor1,valor2):
        pass

class Divisao(Operacao):
    def executar(self,valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Soma(Operacao):
    def executar(self,valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self,valor1, valor2):
        resultado = valor1 - valor2
        return resultado
    
class Multiplicacao(Operacao):
    def executar(self,valor1, valor2):
        resultado = valor1 * valor2
        return resultado





