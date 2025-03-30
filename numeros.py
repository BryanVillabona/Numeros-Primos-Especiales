def encontrar_numeros_primos(limite):
    primos = []
    
    for num in range(2, limite + 1):
        rta = 0
        for i in range(1, num + 1):
            if num % i == 0:
                rta += 1

        if rta == 2:
            primos.append(num)

    return primos

def encontrar_primos_gemelos(limite):
    primos = encontrar_numeros_primos(limite)
    gemelos = []

    for i in range(len(primos) - 1):
        if primos[i + 1] - primos[i] == 2:
            gemelos.append((primos[i], primos[i + 1]))

    return print(gemelos)

def es_palindromo(n):
    return str(n) == str(n)[::-1]

def encontrar_primos_palindromicos(limite):
    primos = encontrar_numeros_primos(limite) 
    palindromicos = []  
    
    for num in primos:
        if es_palindromo(num): 
            palindromicos.append(num) 
    
    return print(palindromicos) 
