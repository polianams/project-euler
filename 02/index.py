def fiboEvenSum(n):
    sequencia_fibonati = 1
    sequencia_fibonaci_anterior = 1
    soma_fibonati = 0
    fibonati = []

    while sequencia_fibonati < n:
        proximo_valor = sequencia_fibonati + sequencia_fibonaci_anterior
        sequencia_fibonaci_anterior = sequencia_fibonati
        sequencia_fibonati = proximo_valor
        if proximo_valor <= n and proximo_valor % 2 == 0:
            soma_fibonati += proximo_valor
            fibonati.append(proximo_valor)

    print(soma_fibonati)


fiboEvenSum(8)
fiboEvenSum(10)
fiboEvenSum(34)
fiboEvenSum(60)
fiboEvenSum(1000)
fiboEvenSum(100000)
fiboEvenSum(4000000)
