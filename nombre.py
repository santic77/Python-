nombre_uno = input('Ingresa un nombre ')
edad_uno = int(input(f'{nombre_uno}, cual es su edad? '))
nombre_dos = input('Ingresa un nombre ')
edad_dos = int(input(f'{nombre_dos}, cual es su edad? '))
if edad_uno > edad_dos:
    print(f'{nombre_uno} es mayor que {nombre_dos}')
elif edad_uno < edad_dos:
     print(f'{nombre_dos} es mayor que {nombre_uno}')
else:
    print(f'{nombre_uno} y {nombre_dos} tienen la misma edad')

