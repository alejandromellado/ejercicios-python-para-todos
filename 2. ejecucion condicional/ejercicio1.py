# Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

def main():
    hours = float( input('Introduzca Horas: ') )
    rate = float( input('Introduzca Tarifa: ') )

    salary = 0
    if hours > 40:
        salary = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        salary = hours * rate

    print(f'Salario: {salary}')


if __name__ == '__main__':
    main()
