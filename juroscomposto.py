vi = float(input('Digite o valor inicial:\t'))
i = float(input('Digite a taxa de juros\t'))
i = i/100
n = float(input('Digite o tempo de aplicação\t'))
vf = 0
vf = vi*(1+i)**n
print('O valor depois de',n,'meses é: R$',round(vf))
