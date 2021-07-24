import time
tempo = float(input("Digite o valor do tempo (número de segundos): "))

distância = (tempo*340)

print("A distância do raio é de: {:.2f}".format(distância))

time.sleep(5)
print("O programa foi finalizado")
