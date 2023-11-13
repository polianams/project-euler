function multiplesOf3and5(number) {
  let soma = 0;
  for (let i = number - 1; i > 0; i--) {
    if (i % 3 === 0 || i % 5 === 0) {
      soma += i;
    }
  }
  console.log(soma);
}

multiplesOf3and5(1000);
