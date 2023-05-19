'''
Leia uma frase e gere uma nova frase, retirando os espaços entre as palavras.
'''

def main():
    frase = input('Digite a frase: ')
    frase_nova = frase.replace(' ','') # Função replace tira os espacamento das frases
    print(frase_nova)
main()