import random
import math

numero = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número de 1 a 100: "))
    tentativas += 1

    if palpite == numero:
        print("Acertou!")
        print("Tentativas:", tentativas)
        print("Raiz das tentativas:", math.sqrt(tentativas))
        break
    elif palpite < numero:
        print("Muito baixo!")
    else:
        print("Muito alto!")