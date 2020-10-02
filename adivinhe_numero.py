import random


numero = random.randint(1, 100)

tentativas = 0
chute = 0

print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

while chute != numero:

    tentativas = tentativas + 1

    chute = int(input())

    if chute > numero:
        print("Tente um número menor!")

    if chute < numero:
        print("Tente um número maior!")

print(f"Parabéns! Você acertou na tentativa {tentativas}.")
