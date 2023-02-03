# Ejercicio 2: Este programa cuenta la distribución de la hora del día
# para cada uno de los mensajes. Puedes extraer la hora de la línea
# “From” buscando la cadena horaria y luego dividiendo la cadena en
# partes utilizando el carácter colon. Una vez que hayas acumulado las
# cuentas para cada hora, imprime las cuentas, una por línea, ordenadas
# por hora tal como se muestra debajo.

# python timeofday.py
# Ingresa un nombre de archivo: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            counter = {}
            for line in file:
                # dividir linea en palabras y revisar si es relevante
                words = line.split()
                if not words or words[0] != 'From':
                    continue

                hour = words[5].split(':')[0]
                if hour not in counter:
                    counter[hour] = 1
                else: counter[hour] += 1

            for t in sorted(list(counter.items())):
                print(t)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
