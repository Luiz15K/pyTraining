turno = input('Informe o periodo em que voce estuda: ').upper()

def verificaTurno(meuTurno):
    retorno = ''
    if meuTurno == 'MATUTINO' :
        retorno = 'Bom dia>>>'
    elif meuTurno == 'VESPERTINO':
        retorno = 'Boa tarde>>>'
    elif meuTurno == 'NOTURNO':
        retorno = 'Boa noite>>>'
    else:
        retorno = 'Valor invalido !!!'

    return retorno

pegaRetorno = ''
pegaRetorno = verificaTurno(turno)

print(pegaRetorno)
