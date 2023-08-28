lista=''
print('Para finalizar digite "0" e aperte "ENTER"')
while True:
    texto=input('Digite: ')
    if texto=='0':
        print('Programa finalizado')
        break
    else:
        lista=lista+texto
print(lista)