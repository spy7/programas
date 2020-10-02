from random import randint
from time import sleep


def limpa_tela():
    print('\33c')


def desenha_cavalo(distancia):
    print (" " * distancia + "\u250C\u2524")


def desenha_pista(distancia):
    print ("-" * distancia)


def desenha_corrida(tamanho, cavalos):
    desenha_pista(tamanho + 2)
    for cavalo in cavalos:
        desenha_cavalo(cavalo)
        desenha_pista(tamanho + 2)


def retorna_lider(cavalos):
    frente = max(cavalos)
    return [
        cavalo + 1
        for cavalo, distancia in enumerate(cavalos)
        if distancia == frente
    ]


def escreve_lider(cavalos):
    print(f"Cavalo na frente: {retorna_lider(cavalos)}")


def sorteio():
    return randint(1, 2)


cavalos = [0, 0, 0]
tamanho = 50

numeros_cavalos = list(range(1, len(cavalos) + 1))

limpa_tela()
desenha_corrida(tamanho, cavalos)

aposta = 0
while aposta not in numeros_cavalos:
    print(f"Qual cavalo vai ganhar? {numeros_cavalos}")
    aposta = int(input())

while not any(cavalo >= tamanho for cavalo in cavalos):
    cavalos = [cavalo + sorteio() for cavalo in cavalos]
    limpa_tela()
    desenha_corrida(tamanho, cavalos)
    escreve_lider(cavalos)
    sleep(0.5)

lider = retorna_lider(cavalos)
if aposta in lider:
    print("Parabéns!!! Você acertou!")
else:
    print("Que pena! Seu cavalo não chegou na frente")
