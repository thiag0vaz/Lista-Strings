'''
Leia uma data no formato DD/MM/AAAA e escreva o mês por extenso (DD de mês de AAAA).
'''

def main():
    dia, mes, ano = map(int, input('Digite uma data (DD/MM/AAAA): ').split('/'))
    if mes == 1:
        print(f'{dia} de Janeiro de {ano}')
    elif mes == 2:
        print(f'{dia} de Fevereiro de {ano}')
    elif mes == 3:
        print(f'{dia} de Março de {ano}')
    elif mes == 4:
        print(f'{dia} de Abril de {ano}')
    elif mes == 5:
        print(f'{dia} de Maio de {ano}')
    elif mes == 6:
        print(f'{dia} de Junho de {ano}')
    elif mes == 7:
        print(f'{dia} de Julho de {ano}')
    elif mes == 8:
        print(f'{dia} de Agosto de {ano}')
    elif mes == 9:
        print(f'{dia} de Setembro de {ano}')
    elif mes == 10:
        print(f'{dia} de Outubro de {ano}')
    elif mes == 11:
        print(f'{dia} de Novembro de {ano}')
    elif mes == 12:
        print(f'{dia} de Dezembro de {ano}')
    
main()