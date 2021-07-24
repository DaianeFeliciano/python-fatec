import time
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = (base * altura) / 2

print(" O valor da base informado é {:.2f} \n A altura informada é {:.2f} "
      "\n O cálculo da área do triângulo é {:.2f}".format(base, altura, area))

time.sleep(5)
print(" O programa foi finalizado")
