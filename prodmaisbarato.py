#PRODUTO MAIS BARATO
barato = [3.99,"arroz"]
while True:
        resu1 = str(input('Informe o valor do primeiro produto: '))
        resu2 = float(input('Informe o valor do segundo produto: '))
        resu3 = float(input('Informe o valor do terceiro produto: '))
        barato.append(resu1)
        barato.append(resu2)
        barato.append(resu3)
        if resu1 < resu2:
            print('O valor do primeiro produto e o mais barato',resu1)
        elif resu2 < resu3:
            print('O valor do segundo produto e o mais barato',resu2)
        elif resu3 < resu2:
            print('O terceiro produto esta em conta',resu3)
        else:
            print('Erro!!,\nDigite novamente o valor\n')