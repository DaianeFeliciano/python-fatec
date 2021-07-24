"""− Se o número de lados for igual a 5 imprime “PENTÁGONO”, calcule e mostre a área do pentágono.
(Pesquise no google com se calcula a area de um PENTAGONO)
Acrescente as seguintes mensagens ao exercício 1 conforme o caso.
− Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
− Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO."""

from math import sqrt, pow
NumLados = float(input("Digite o número de lados do polígono regular: "))
if NumLados == 3:
    print("\033[35m É um TRIÂNGULO! \033[m")
    print("\033[36m=*\033[m"*20)
    MedLado = float(input("Digite a medida do lado do polígono regular: "))
    print("\033[36m=*\033[m" * 20)
    p = (MedLado*3) / 2
    area = sqrt(p*(p-MedLado)*(p-MedLado)*(p-MedLado))
    print("\033[35mA área do triângulo é {:.2f}\033[m".format(area))
elif NumLados == 4:
    print("\033[31m É um QUADRADO! \033[m")
    print("\033[30m=*\033[m" * 20)
    MedLado = float(input("Digite a medida do lado do polígono regular: "))
    print("\033[30m=*\033[m" * 20)
    area = pow(MedLado,2)
    print("\033[31mA área do quadrado é {:.2f}\033[m".format(area))
elif NumLados ==5:
    print("\033[33m É um PENTÁGONO!\033[m")
    print("\033[34m=*\033[m" * 20)
    MedLado = float(input("Digite a medida do poligono regular: "))
    print("\033[34m=*\033[m" * 20)







