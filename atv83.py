import sys

tecla = 0
contvldias = 0
vlacumulador = 0

while tecla != 3:
    tecla = int(input("\nMenu\n1 Leitura\n2 Exibir\n3 Sair\nItem:"))

    if tecla == 1:
        valor = float(input("Digite o valor da prestação: R$ "))
        vlacumulador = vlacumulador + valor
        dias = int(input("Digite a quantidade de dias em atraso: "))
        contvldias = contvldias + dias
        multa = (2/100) * vlacumulador
        txjuros = (1/100)
        vljuros = (txjuros/30) * dias * vlacumulador
        vlpagar = vlacumulador + vljuros + multa
    elif tecla == 2:
        print("O valor da prestação é de R$ {:.2f}\n Quantidade de dias em atraso: {:.2f}\n O valor da multa ficou de "
              "R$ {:.2f}\n "
              "Valor de juros R$ {:.2f}\n Valor total a "
              "pagar R$ {:.2f}".format(vlacumulador,contvldias,multa,vljuros,vlpagar))
    elif tecla == 3:
        break
    else:
        print("Digite novamente, por favor")
print("Fechando a aplicação...")
sys.exit()

