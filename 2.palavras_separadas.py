'''
Leia uma frase e mostre cada palavra da frase em uma linha separada.
'''

def main():
    frase = input('Digite a frase: ')
    separacao = frase.split()
    for separacao in separacao:
        print(separacao)    
          
main()