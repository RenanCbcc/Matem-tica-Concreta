import sys
import math
from numpy import linspace
from fractions import Fraction

class Menu:
    def __init__(self):
        self.escolhas = {
            "1": self.__primeira_questao,
            "2": self.__segunda_questao,
            "3": self.__terceira_questao,
            "4": self.__quarta_questao,
            "5": self.__quinta_questao,
            "6": self.__sexta_questao,
            "7": self.__setima_questao,
            "8": self.__oitava_questao,
            "9": self.__nona_questao,
            "10":self.__decima_questao,
            "0": self.__sair
        }

    def apresentar_menu(self):
        print("""
            Menu
            1ª. Questão
            2ª. Questão
            3ª. Questão
            4ª. Questão
    	    5ª. Questão
            6ª. Questão
            7ª. Questão
            8ª. Questão
            9ª. Questão
            10ª Questão
            """)

    def executar(self):
        while True:
            self.apresentar_menu()
            escolha = input("Escolha uma opção (0-10):")
            acao = self.escolhas.get(str(escolha))
            if acao:
                acao()
            else:
                print("{0} não foi uma escolha válida.".format(escolha))

    def __primeira_questao(self):
        print("1) Qual o primeiro múltiplo de 17 maior que 1000?")
        for i in range(100):
            multiplo = 17 * i
            if (multiplo >= 1000):
                print(multiplo)
                break


    def __segunda_questao(self):
        print("Quantos multiplos de 17 existem no intervalo [1000,7000]?")
        s = 0
        for i in range(1,412):
            multiplo = 17 * i
            if (multiplo >= 1000 and multiplo <= 7000):
                print(multiplo)
                s+=1
        print("Há %i multiplos de 17 no intervalo [1000,7000]" %s)

    def __terceira_questao(self):
        print("Determine o primeiro termo da Pg maior 20 e a sua ordem. a1=2, q=1,02")
        print("Termo geral dado por an = 1,960784314 * 1,02^n")

        n = 1
        while(20>=(1.960784314 * math.pow(Fraction(1.02).limit_denominator(),n))):
            n+=1

        print("%f = 1,960784314 * 1,02^ %i"%((1.960784314 * math.pow(Fraction(1.02).limit_denominator(),n)),n))


    def __quarta_questao(self):
        print("x = (Σ[k = 1, n = 20] k²) ÷ Π[k=10, n = 100] ln (k)")

        s= 0
        p= 1
        for i in range(1,21):
            s+= math.pow(i,2)

        for i in range(10, 101):
            p*= math.log(i)

        print("Resultado: %f"%(s/p))

    def __quinta_questao(self):
       print("Seis crianças escolhem um pirulito entre  uma seleção de vermelhos"
             ", amarelos e verdes. de quantas maneiras isto pode ser feito? Não importa"
             "que criança obtem o quê."
             "Calcule CR(n,r).")

       print("CR(n+r-1,r)")
       print("CR(6+3-1,6)")
       print("CR(6+3-1,6)")
       print("CR(8,6)")
       print(self.__Combination(8,6))

    def __sexta_questao(self):
        print("Calcule n, de modo que f(n) = n²+5n-200 enteja no intervalo [-5,50].")

        for n in range(-5, 51):
            print(n, math.pow(n, 2) + 5 * n - 200)

    def f(self,x):
        return math.pow(x,3)-(2*math.pow(x,2))-x-200


    def __setima_questao(self):
        print("Resolver x³-2x²-x-200=0 para x>0 por força bruta.")



    def __oitava_questao(self):
        print("Listar o trinagulo de pascal 5 linhas.")
        for n in range(6):
            for r in range(6):
                if (r - n) >= 0:
                    print(self.__Combination(r,n))

    def __nona_questao(self):
        print("Quantos termos da PA{3,6,9,12} exitem entre 350 e 3160?")
        n = 350
        while (350 >= 3*n and 3*n <= 3160):
            n += 1

        print("[350 >= 3*n and 3*n <= 3160]: %i"%n)

    def __decima_questao(self):
        print("Determine uma aproximação para a raiz positiva da equação: x³+x-100=0")

    def __sair(self):
        print("Saindo...")
        sys.exit(0)

    def __Permutation(self,n,r):
        return math.factorial(n)/math.factorial(n-r)

    def __Combination(self,n, r):
        return self.__Permutation(n, r) / math.factorial(r)


if __name__ == "__main__":
	    m = Menu()
	    m.executar()