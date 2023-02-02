# Ejercicio 2: Escribe otro programa que pida una lista de números como
# la anterior y al final muestre por pantalla el máximo y mínimo de los
# números, en vez de la media.

def main():
    numbers = []
    while True:
        try:
            entry = input('Introduzca un número: ')
            if entry == 'fin':
                break
            numbers.append(float(entry))
        except ValueError:
            print('Entrada inválida')

    print(f'minimo: {min(numbers)}, maximo: {max(numbers)}')


if __name__ == '__main__':
    main()
