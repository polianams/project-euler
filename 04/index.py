def smallestMult(n):
    condicao = False
    numero = 1
    contagem = 0

    while condicao == False:
        menor_numero = numero
        contagem = 0
        for i in range(1, n + 1):
            if numero % i == 0:
                contagem += 1

        if contagem == n:
            menor_numero = numero
            return menor_numero

        numero += 1


print(smallestMult(5))
print(smallestMult(7))
print(smallestMult(10))
print(smallestMult(13))
