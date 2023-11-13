def largestPrimeFactor(number):
    verificar_numero = 2
    numeros_primos = []

    if number == 1:
        return number
    else:
        while verificar_numero <= number:
            if number % verificar_numero == 0:
                primo = True
                for i in numeros_primos:
                    if verificar_numero % i == 0:
                        primo = False
                        break
                if primo:
                    numeros_primos.append(verificar_numero)
            verificar_numero += 1

        return max(numeros_primos)


print(largestPrimeFactor(2))
print(largestPrimeFactor(3))
print(largestPrimeFactor(5))
print(largestPrimeFactor(7))
print(largestPrimeFactor(8))
print(largestPrimeFactor(13195))
