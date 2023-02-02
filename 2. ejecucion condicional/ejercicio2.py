# Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
# programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
# un mensaje y saliendo del programa.

def main():
    hours, rate = 0, 0
    try:
        hours = float( input('Introduzca Horas: ') )
        rate = float( input('Introduzca Tarifa: ') )
    except ValueError:
        print('Error, por favor introduzca un número')
        exit(1)

    print(f'Salario: {hours * rate}')


if __name__ == '__main__':
    main()
