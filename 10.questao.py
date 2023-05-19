def main():
    palavra = input('Digite a palavra: ')
    reversa = palavra[::-1]
    if palavra == reversa:
        print('É palindroma')
    else:
        print('Não é palindroma')
main()