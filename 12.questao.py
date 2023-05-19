def main():
    nome_completo = input('Digite seu nome: ')
    
    nomes = nome_completo.split() 
    
    sobrenome = nomes[-1]
    nome = nomes[0]
    
    print(f'{sobrenome} / {nome}')
main()