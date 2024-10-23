salario = float(input("Digite o salario do funcionário:"))
percentual = float(input("Digite o % de aumento:"))
calculo = 0
novosalario = 0
calculo = (salario*percentual) / 100
novosalario = salario + calculo
print('O valor do aumento é',calculo)
print('Seu novo salario é',novosalario)
