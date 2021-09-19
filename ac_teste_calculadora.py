import unittest
from ac_calculadora import Calculadora

class Testes_operacoes(unittest.TestCase):
    def teste_divisao(self):
        calculadora_divisao = Calculadora()
        self.assertEqual(calculadora_divisao.calcular(10,2,"Divisao"), 5)


    def teste_soma(self):
        calculadora_soma = Calculadora()
        self.assertEqual(calculadora_soma.calcular(10,10,"Soma"), 20)


    def teste_subtracao(self):
        calculadora_subtracao = Calculadora()
        self.assertEqual(calculadora_subtracao.calcular(10,9,"Subtracao"), 1)


    def teste_multiplicacao(self):
        calculadora_multiplicacao = Calculadora()
        self.assertEqual(calculadora_multiplicacao.calcular(10,5,"Multiplicacao"), 50)

    def teste_erro_divisao(self):
        calculadora_divisao = Calculadora()
        self.assertEqual(calculadora_divisao.calcular(10,2,"Divisa"), "ERRO" )

    def teste_erro_soma(self):
        calculadora_soma = Calculadora()
        self.assertEqual(calculadora_soma.calcular(10,10,"Som"), "ERRO" )

    def teste_erro_subtracao(self):
        calculadora_subtracao = Calculadora()
        self.assertEqual(calculadora_subtracao.calcular(10,9,"Subtraca"), "ERRO")

    def teste_erro_multiplicacao(self):
        calculadora_multiplicacao = Calculadora()
        self.assertEqual(calculadora_multiplicacao.calcular(10,5,"Multiplicaca"), "ERRO")
    


        
if __name__ == '__main__':
    unittest.main()