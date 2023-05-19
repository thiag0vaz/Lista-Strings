def main():
    nome_completo = input('Digite seu nome: ')
    
    nomes = nome_completo.split() 
    
    sobrenome = nomes[-1]
    nome1 = nomes[0]
    
    for letras in nome1[0]:
        inicial1 = letras[0]
    
    nome2 = nomes[1]
    
    for letras in nome2[0]:
        inicial2 = letras[0]
    
    print(f'{sobrenome}, {inicial1.upper()}. {inicial2.upper()}')
    
main()