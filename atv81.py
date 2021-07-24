"""Faça um algoritmo para ler uma lista de NOMES, SALARIOS e IDADES, qualquer, ao final
exiba a quantidade de pessoas lidas (CONTPES), a média de salários (MEDIASAL) e a
média de idades (MEDIAIDA). Crie um Menu Repetitivo com while."""

import sys
menu = 0
while !=
while 2 != tecla:

    tecla = int(input("\nMenu\n1 Leitura e Exibir\n2 Sair\nItem:"))

    if tecla == 1:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        if a < b + c and b < a + c and c < a + b:
            p = (a + b + c) / 2
            area = sqrt(p * (p - a) * (p - b) * (p - c))
            triangulo = True

        else:
            triangulo = False
        if triangulo == True:
            print("Tratasse de um triângulo")
            if a == b and a == c and b == c:
                print("É um triângulo EQUILÁTERO! \n O semiperímetro é {:.2f} A área do triângulo é {:.2f}".format(p, area))
            elif a != b and a != c and b != c:
                print("É um triângulo ESCALENO!\n \n O semiperímetro é {:.2f} A área do triângulo é {:.2f}".format(p, area))
            elif a == b and a != c or a == c and a != b or b == c and b != a:
                print("É um triângulo ISÓSCELES! \n O semíperímetro {:.2f} sem A área do triângulo é {:.2f}".format(p,area))
        else:
            print("Uma figura qualquer de três lados")
    elif tecla == 2:
        break
    else:
        print("Digite novamente por favor")

print("Fechando aplicação")
sys.exit()