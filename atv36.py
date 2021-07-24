"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

distancia = float(input("Digite o Km da viagem: "))
if distancia <= 200:
    cv = (distancia*0.50)
    print("O preço da passagem é de R$ {} ".format(cv))
else:
    cv2 = (distancia*0.45)
    print("O preço da passagem é de R$ {}".format(cv2))