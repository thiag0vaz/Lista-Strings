def main():    
    entrada = input('Digite a frase, posição incial, comprimento: ')
    valor = entrada.split(',')
    texto = valor[0]
    posicao = int(valor[1])
    comprimento = int(valor[2])
    resultado = substr(texto, posicao, comprimento)
    print(resultado)

def substr(texto, posicao, comprimento):
    return texto[posicao : posicao + comprimento]

main()