def main():
    cadastro = input('Cadastre sua senha: ')
    login = input('Digite sua senha: ')
    mostrador = len(cadastro) * '*'
    
    if cadastro == login:
        print(f'Sua senha {mostrador} está correta')
    else:
        print(f'Sua senha está incorreta. Você digitou {login}')
        
main()