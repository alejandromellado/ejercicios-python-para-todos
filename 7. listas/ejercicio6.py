# Ejercicio 6: Reescribe el programa que pide al usuario una lista de
# números e imprime el máximo y el mínimo de los números al final cuando
# el usuario ingresa “hecho”. Escribe el programa para almacenar los
# números que el usuario ingrese en una lista, y utiliza las funciones max()
# y min() para calcular el máximo y el mínimo después de que el bucle
# termine.
# Ingresa un número: 6
# Ingresa un número: 2
# Ingresa un número: 9
# Ingresa un número: 3
# Ingresa un número: 5
# Ingresa un número: hecho
# Máximo: 9.0
# Minimo: 2.0

def get_numbers():
    numbers = []
    while True:
        try:
            entry = input('Introduzca un número: ')
            if entry == 'hecho':
                break
            numbers.append(float(entry))
        except ValueError:
            print('Entrada inválida')

    return numbers


def main():
    numbers = get_numbers()
    print(f'Máximo: {max(numbers)}')
    print(f'Minimo: {min(numbers)}')


if __name__ == '__main__':
    main()
