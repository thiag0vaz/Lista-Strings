def main():
    entrada = input('Digite a coluna e a palavra a ser expressa: ')
    valores = entrada.split(',')
    coluna = int(valores[0])
    texto = valores[1]
    resultado = vertical(coluna, texto)
    print(resultado) 

def vertical(coluna, texto):
    espacos = ' ' * coluna
    for caractere in texto:
        if len(texto) > 20:
            print('O texto deve conter no máximo 20 letras')
        else: 
            print(espacos + caractere)
            espacos += ''

main()