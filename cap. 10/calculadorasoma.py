while True:
    numero1 = input('digite o primeiro numero: ')
    
    numero2 = input('digite o segundo numero: ')

    try : 
        soma = int(numero1) + int(numero2)
    except ValueError:
        print('digite apenas valores numericos')
    else:
        print(soma)