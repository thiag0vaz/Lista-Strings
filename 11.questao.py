'''
Um dos recursos disponibilizados pelos editores de texto mais modernos é a contagem da quantidade de
palavras de um texto. Escreva um programa que determine o numero de palavras de um texto digitado.
'''

def main():
    frase = input('Digite o texto: ')
    quantidade = contar_palavras(frase)
    print(quantidade)

def contar_palavras(frase):
    contador = frase.split()
    return len(contador)

main()