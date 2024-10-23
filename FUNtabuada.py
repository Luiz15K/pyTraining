#tabuada
#def tabuada (valor1):
#    resu1 = valor1 * 1
#    resu2 = valor1 * 2
#    resu3 = valor1 * 3
#    resu4 = valor1 * 4
#    resu5 = valor1 * 5
#    resu6 = valor1 * 6
#    resu7 = valor1 * 7
#    resu8 = valor1 * 8
#    resu9 = valor1 * 9
#    resu10 = valor1 * 10
#   return [resu1,resu2,resu3,resu4,resu5,resu6,resu6,resu7,resu8,resu9,resu10]

#def tabuada(valor1):
#    for resu in range(1,11):
#        print('{0} x {1} = {2}'.format(valor1,resu,valor1*resu))

inicio = 1
final = 11

def tabuada(valor1):
    auxiliar = ''
    for resu in range(inicio, final):
        auxiliar += '{0} x {1} = {2}\n'.format(valor1,resu,valor1*resu)
    return auxiliar
