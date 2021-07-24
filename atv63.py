from math import sqrt, pow
import sys
menuchoice = 0
while menuchoice != 4:

    menuchoice = int(input("\nMenu\n1 Leitura\n2 Calcular\n3 Exibir\n4 Sair\nItem: "))
    if menuchoice == 1:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
    else:
        if menuchoice == 2:
            delta = (b ** 2 - 4 * a * c)

        else:
            if menuchoice == 3:
                if a == 0:
                    print("Valor de a tem que ser diferente de zero")
                else:
                    if delta > 0 or delta == 0:
                        raiz = sqrt(delta)
                        a2 = 2 * a
                        x1 = (-b + raiz) / a2
                        x2 = (-b - raiz) / a2
                        print("O delta da equacão de 2º grau é {}\n A raiz de delta é {} "
                              "\ne x1 = {} e "
                              "x2 = {}".format(
                            delta, raiz, x1, x2))
                    else:
                        print("Sem solução no conjunto dos números reais")
            else:
                if menuchoice == 4:
                    print("Programa finalizado")
                    sys.exit()
                else:
                    print("Menu inválido")
