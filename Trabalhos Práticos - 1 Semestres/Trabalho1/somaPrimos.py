def somaPrimos(primo):
    """dado um número primo, retorna todos os números primos menores que esse 
       e a soma de todos esses
       int -> string"""

    primos = []
    divisoresPrimo = 0
    for numeros in range(2,primo):
        if primo%numeros == 0:
                divisoresPrimo += 1
                
    if (divisoresPrimo == 0):

        for i in range(2,primo):
            divisores = 0
            for numeros in range(2,primo):
                if i%numeros == 0:
                    divisores += 1
            if (divisores < 2):
                primos.append(i)
                print(f"O numero {i} é primo")
        print(f"A soma de todos os números primos menores iguas a {primo} é: {sum(primos)}")
    else:
        print("Somente chamar a função com um número primo")

