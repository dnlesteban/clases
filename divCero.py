op1 = float(input('Ingrese primer número: '))
op2 = float(input('Ingrese segundo número: '))

print('Menú')
print('1 - Suma')
print('2 - Resta')
print('3 - Multiplicación')
print('4 - División')

opcion = input('Elija una opción (1, 2, 3 o 4): ')

match opcion:
    case '1':
        r = op1 + op2
    case '2':
        r = op1 - op2
    case '3':
        r = op1 * op2
    case '4':
        try:
            r = op1 / op2
        except ZeroDivisionError:
            print('Error: División por cero')
            r = None
    case _:
        print('Opción inválida')
        r = None

if r is not None:
    print(f'Resultado = {r}')
