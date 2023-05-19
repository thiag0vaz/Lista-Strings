def main():
    entrada = input('Digite a palavra a ser expressa: ')
    coluna = 0
    resultado = vertical(coluna, entrada)
    print(resultado) 

def vertical(coluna, texto):
    espacos = ' ' * coluna
    for caractere in texto:
        if len(texto) > 20:
            print('O texto deve conter no máximo 20 letras')
        else: 
            print(espacos + caractere)
            espacos += ' '

main()