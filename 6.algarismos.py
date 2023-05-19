'''
Leia uma frase e gere uma nova frase, substituindo o algarismo que aparecer na frase por seu extenso.
'''
def main():
    frase = input('Digite a frase: ')
    frase_nova = substituir_algarismos_por_extenso(frase)
    print(frase_nova)

def substituir_algarismos_por_extenso(frase):
    numeros_extenso = {
        "0": "zero",
        "1": "um",
        "2": "dois",
        "3": "três",
        "4": "quatro",
        "5": "cinco",
        "6": "seis",
        "7": "sete",
        "8": "oito",
        "9": "nove"
    }

    nova_frase = ''
    for caractere in frase:
        if caractere.isdigit():
            extenso = numeros_extenso[caractere]
            nova_frase += extenso
        else:
            nova_frase += caractere
    
    return nova_frase

main()