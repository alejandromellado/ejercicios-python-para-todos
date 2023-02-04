# Ejercicio 2: escribe un programa que busque líneas en la forma:
# New Revision: 39772
# Extrae el número de cada línea usando una expresión regular y el
# método findall(). Registra el promedio de esos números e imprímelo.
# Ingresa nombre de archivo: mbox.txt
# 38444.0323119
# Ingresa nombre de archivo: mbox-short.txt
# 39756.9259259
import re


def main():
    filename = '../mbox-short.txt'
    regex = r'New Revision: (\d+)'

    try:
        with open(filename) as file:
            relevant_text = re.findall(regex, file.read())
            foo = [float(entry) for entry in relevant_text]
            print(sum(foo) / len(foo))

    except FileNotFoundError:
        print(f'No se encontro el archivo: {filename}')


if __name__ == '__main__':
    main()
