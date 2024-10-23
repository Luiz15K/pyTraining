#periodo
resultado = ''
while True:
    turno = input('Informe o periodo em que voce estuda: ')
    if turno == 'Matutino' or turno == 'matutino':
        resultado = 'Bom dia'
    elif turno == 'Vespertino' or turno == 'vespertino':
        resultado = 'Boa tarde'
    elif turno == 'Noturno' or turno == 'noturno':
        resultado = 'Boa noite'
    if resultado != '':
        print(resultado)
        break
    else:
        print('erro')
