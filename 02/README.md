# Projeto Euler - Problema 2

## Soma de Termos Pares da Sequência de Fibonacci

### Descrição do Problema

Cada novo número na sequência de Fibonacci é gerado pela soma dos dois números anteriores. Ao começar com 1 e 2, os primeiros 10 números serão:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Considerando os números na sequência de Fibonacci cujos valores não excedem n, encontre a soma dos números pares.

```
function fiboEvenSum(n) {

  return true;
}

fiboEvenSum(10)
```

### Exemplos

- Para `fiboEvenSum(10)` deve retornar um número;
- A função deve somar os números pares de Fibonacci: `fiboEvenSum(8)`` deve retornar 10;
- `fiboEvenSum(10)` deve retornar 10;
- `fiboEvenSum(34)` deve retornar 44;
- `fiboEvenSum(60)` deve retornar 44;
- `fiboEvenSum(1000)` deve retornar 798;
- `fiboEvenSum(100000)` deve retornar 60696;
- `fiboEvenSum(4000000)` deve retornar 4613732;
