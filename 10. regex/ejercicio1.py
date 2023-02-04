# Ejercicio uno: escribe un programa simple que simule la operación del
# comando grep en Unix. Debe pedir al usuario que ingrese una expresión
# regular y cuente el número de líneas que coincidan con ésta:
# $ python grep.py
# Ingresa una expresión regular: ^Author
# mbox.txt tiene 1798 líneas que coinciden con ^Author
# $ python grep.py
# Ingresa una expresión regular: ^X-
# mbox.txt tiene 14368 líneas que coinciden con ^X-
# $ python grep.py
# Ingresa una expresión regular: java$
# mbox.txt tiene 4175 líneas que coinciden con java$
import re


def main():
    filename = '../mbox.txt'
    regex = input('Ingresa una expresión regular: ')

    try:
        with open(filename) as file:
            i = 0
            for line in file:
                line = line.rstrip()
                if re.search(regex, line):
                    i += 1
            print(f'{filename} tiene {i} líneas que coinciden con {regex}')

    except FileNotFoundError:
        print(f'No se encontro el archivo: {filename}')


if __name__ == '__main__':
    main()
