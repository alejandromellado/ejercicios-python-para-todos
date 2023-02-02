# Ejercicio 3: Escribe un programa para pedirle al usuario el número de
# horas y la tarifa por hora para calcular el salario bruto.

def main():
    hours = float( input('Introduzca Horas: ') )
    rate = float( input('Introduzca Tarifa: ') )
    print(f'Salario: {hours * rate}')


if __name__ == '__main__':
    main()
