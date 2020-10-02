def limpa_tela():
    print('\33c')


def desenha_forca(erros):
    print(' +---------+')
    print(' |         |')
    print(' |         ' + ('o' if erros > 0 else ' '))
    print(' |       ' + ('--' if erros > 2 else '  ') + ('+' if erros > 1 else ' ') + ('--' if erros > 3 else '  '))
    print(' |         ' + ('|' if erros > 4 else ' '))
    print(' |        ' + ('+' if erros > 5 else ' ') + ('+' if erros > 4 else ' ') + ('+' if erros > 6 else ' '))
    print(' |        ' + ('|' if erros > 5 else ' ') + ' ' + ('|' if erros > 6 else ' '))    
    print('-+-')


def escreve_palavra(palavra, chute):
    print('Palavra: ' + ''.join(letra if letra in chute else '-' for letra in palavra))


print('Escreva uma palavra')

palavra = input()

chute = set()

erros = 0

limpa_tela()

print("Tente adivinhar a palavra!")

while erros < 7 and len(set(palavra) - chute) > 0:

    desenha_forca(erros)
    escreve_palavra(palavra, chute)
    
    print("Diga uma letra!")

    letra = input()

    limpa_tela()

    if len(letra) != 1 or letra < 'a' or letra > 'z' or letra in chute:
        print("Letra inválida! Tente novamente!")
        continue

    chute.add(letra)

    if letra not in palavra:
        erros += 1
        print(f"Não tem a letra: {letra}")
    else:
        print("Muito bem!")

desenha_forca(erros)
escreve_palavra(palavra, chute)

if erros >= 7:
    print(f"Você não adivinhou!!! A palavra era {palavra}")
else:
    print("Parabéns!!! Você adivinhou a palavra!!!")
