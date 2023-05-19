def main():
    nome = input('Digite seu nome completo: ')
    login = definir_login(nome)
    print(f'Seu Login: {login}')

def definir_login(nome):
    login = ''
    nomes = nome.split()

    for letras in nomes:
        login += letras[0].lower()

    return login

main()