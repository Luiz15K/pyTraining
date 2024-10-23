#CALCULAR JUROS SIMPLES

valoraplicado = float(input('Digite o valor aplicado\t'))
juros = float(input('Digite o percentual de juros\t'))
tmpaplicaçao = float(input('Digite o tempo de aplicação\t'))
resultado = 0
juros = (juros/100)
resultado = (valoraplicado*juros*tmpaplicaçao)
print(resultado)
