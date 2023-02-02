# Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-y-
# media para las horas extras, y crea una función llamada calculo_salario
# que reciba dos parámetros (horas y tarifa).

def calculo_salario(horas, tarifa):
    if horas > 40:
        return (40 * tarifa) + ((horas - 40) * (tarifa * 1.5))
    return horas * tarifa


def main():
    horas, tarifa = 0, 0
    try:
        horas = float( input('Introduzca Horas: ') )
        tarifa = float( input('Introduzca Tarifa: ') )
    except ValueError:
        print('Error, por favor introduzca un número')
        exit(1)

    salario = calculo_salario(horas, tarifa)
    print(f'Salario: {salario}')


if __name__ == '__main__':
    main()
