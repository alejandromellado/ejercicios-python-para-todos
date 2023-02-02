# Ejercicio 2: Escribe un programa que solicite un nombre de archivo
# y después lea ese archivo buscando las líneas que tengan la siguiente
# forma:

# X-DSPAM-Confidence: 0.8475

# **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla
# aparte para extraer el número decimal de la línea. Cuenta esas líneas y después
# calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al
# final del archivo, imprime el valor medio de “spam confidence”.

# Ingresa un nombre de archivo: mbox.txt
# Promedio spam confidence: 0.894128046745
# Ingresa un nombre de archivo: mbox-short.txt
# Promedio spam confidence: 0.750718518519
# Prueba tu programa con los archivos mbox.txt y mbox-short.txt.


def main():
    filename = input('Ingresa un nombre de archivo: ')
    try:
        file = open(filename)
        values = []
        for line in file:
            if 'X-DSPAM-Confidence:' not in line:
                continue
            start = line.find(':') + 1
            new_value = float(line[start:])
            values.append(new_value)
        print(f'Promedio spam confidence: {sum(values) / len(values)}')

    except FileNotFoundError:
        print(f'No se puede abrir el archivo: {filename}')
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
