'''
Faça a criptografia de uma frase digitada pelo usuário. Na criptografia, a frase deverá ser invertida e as
consoantes deverão ser substituídas pelo caractere #.
'''

def main():
    frase = input('Digite a frase: ')

    frase_criptografada = criptografar_frase(frase)

    print('Frase criptografada:', frase_criptografada)


def criptografar_frase(frase):
    
    frase_invertida = frase[::-1]       # [::-1] Inverte a frase!
    
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  # Tem método mais simples.
    
    frase_criptografada = ''
    for letra in frase_invertida:
        if letra in consoantes:
            frase_criptografada += '#'
        else:
            frase_criptografada += letra
    
    return frase_criptografada

main()