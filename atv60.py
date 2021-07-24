from math import tan, sqrt, pow, radians

NumLados = float(input("Digite o número de lados do polígono regular: "))
MedLado = float(input("Digite a medida do lado do polígono regular: "))

if NumLados < 3:
  print("Não é POLÍGONO!")
elif NumLados > 5:
    print("POLÍGONO NÃO IDENTIFICADO!")
elif NumLados == 3:
    t = "triângulo"
    print("É um ", t)
    p = (MedLado*3) / 2
    area = sqrt(p*(p-MedLado)*(p-MedLado)*(p-MedLado))
    print("A área do triângulo é {:.2f}".format(area))
elif NumLados == 4:
    q = "quadrado"
    print("É um ", q)
    area = pow(MedLado,2)
    print("A área do quadrado é {:.2f}".format(area))
elif NumLados ==5:
    p = "pentágono"
    print("É um ", p)
    area = 5*MedLado/2*(MedLado/(2*(tan((radians(90 - ((5-2)*180/5)/2))))))
    print("A área do pentágono é {:.2f}".format(area))