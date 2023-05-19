def main():
    horas, minutos, segundos = map(int, input().split(':'))
    if segundos > 60:
        minutos = minutos + (segundos // 60)
        segundos = segundos % 60
    
    if minutos > 60:
        horas = horas + (minutos//60)
        minutos = minutos % 60 
        
    if segundos > 3600:
        horas += 1
    
            
    print(f'{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')
main()