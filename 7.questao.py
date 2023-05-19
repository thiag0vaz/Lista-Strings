def main():
    frase = input('Digite o verbo regular: ')
    nova_frase = letras(frase)
    print(nova_frase)
            
def letras(frase):
    resultado = frase[:-1]
    return resultado 
        
main()