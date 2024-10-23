import datetime as dt
programa = int(input('Qual o tamanho do programa que deseja baixar?: '))
velonet = int(input('Qual a velocidade da sua internet contratada?: '))
if programa > 1024:
    print('O tamanho inserido do programa possui:',programa/1000,'GB')
else:
    print('O tamanho inserido do programa possui:',programa,'MB')
programa = programa*1000/8
valorprog = programa/velonet
resultado = valorprog/60
if resultado > 60:
    hora = resultado/60
    minuto = resultado % 60
    print('Faltam aproximadamente',round(hora),'horas e',round(minuto),'minutos')
elif resultado < 60:
    hora = resultado/60
    minuto = resultado % 60
    print('Faltam aproximadamente',round(minuto),'minutos')
else:
    print('Faltam aproximadamente', minuto ,'minutos para o término da solução.')
hora_atual = dt.datetime.now()
hora_dia = dt.datetime.now()
hora_final = hora_atual + dt.timedelta(minutes = resultado)
hora_atual = hora_atual.strftime('%H:%M %p')
hora_final = hora_final.strftime('%H:%M %p')
hora_dia = hora_dia.strftime('%d')
print('O horário atual é',hora_atual)
print('O horário final do download será aproximadamente as',hora_final,'do dia',hora_dia)

