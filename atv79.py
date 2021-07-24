from datetime import date
import sys
tecla = int( input ("\nMenu\n1 Executar \n2 Sair\nItem:"))
if tecla == 1:
    ano = int(input("Que ano quer analisar? Coloque 0 para anlisar o ano atual: "))
    b = "bissexto"
    nb = "não é bissexto"
    if ano == 0:
        ano = date.today().year #ano atual
    if ano % 4 ==0 and ano % 100 !=0 or ano % 400 ==0:
        print("O ano {} é {}".format(ano,b))
    else:
        print("O ano {} {}".format(ano, nb))
elif tecla ==2:
    sys.exit ()