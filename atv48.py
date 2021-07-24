from math import sqrt, pow, tan, radians

def digita_lados():
    NumLados = float(input("Digite o número de lados do polígono regular: "))
    valida_lados(NumLados)

def valida_lados(NumLados):
    if NumLados < 3:
        print("\033[35;40mNão é POLÍGONO!\033[m")
        digita_lados()
    elif NumLados > 5:
        print("\033[35;40mPOLÍGONO NÃO IDENTIFICADO!\033[m")
        digita_lados()
    else:
        calcula_areas(NumLados)

def calcula_areas(NumLados):
    MedLado = float(input("Digite a medida do lado do polígono regular: "))
    if NumLados == 3:
        print("\033[35m É um TRIÂNGULO! \033[m")
        print("\033[36m=*\033[m" * 20)
        p = (MedLado * 3) / 2
        area = sqrt(p * (p - MedLado) * (p - MedLado) * (p - MedLado))
        print("\033[35mA área do triângulo é {:.2f}\033[m".format(area))
    elif NumLados == 4:
        print("\033[31m É um QUADRADO! \033[m")
        print("\033[30m=*\033[m" * 20)
        area = pow(MedLado, 2)
        print("\033[31mA área do quadrado é {:.2f}\033[m".format(area))
    elif NumLados == 5:
        print("\033[33m É um PENTÁGONO!\033[m")
        print("\033[34m=*\033[m" * 20)
        area = 5 * MedLado / 2 * (MedLado / (2 * (tan((radians(90 - ((5 - 2) * 180 / 5) / 2))))))
        print("\033[33mA área do pentágono é {:.2f} \033[m".format(area))

digita_lados()
