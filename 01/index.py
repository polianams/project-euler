def multiplesOf3and5(number):
    soma_total = 0
    i = 1
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            soma_total += i
        i += 1
    print(soma_total)


multiplesOf3and5(10)
multiplesOf3and5(49)
multiplesOf3and5(1000)
multiplesOf3and5(8456)
multiplesOf3and5(19564)
