'''
Leia uma frase e gere uma nova frase, duplicando cada caractere da frase digitada.
'''

def main():
    frase = input('Digite a frase: ')
    frase_duplicada = ''
    for caractere in frase:
        frase_duplicada += caractere * 2
        
    print(frase_duplicada)
main()