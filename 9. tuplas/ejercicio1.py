# Ejercicio 1: Revisa el programa anterior de este modo: Lee y analiza
# las líneas “From” y extrae las direcciones de correo. Cuenta el número
# de mensajes de cada persona utilizando un diccionario.
# Después de que todos los datos hayan sido leídos, imprime la persona con
# más envíos, creando una lista de tuplas (contador, email) del diccionario.
# Después ordena la lista en orden inverso e imprime la persona que tiene
# más envíos.
# Línea de ejemplo:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Ingresa un nombre de archivo: mbox-short.txt
# cwen@iupui.edu 5
# Ingresa un nombre de archivo: mbox.txt
# zqian@umich.edu 19

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

                sender = words[1]
                if sender not in counter:
                    counter[sender] = 1
                else: counter[sender] += 1

            result = sorted(list(counter.items()), key=lambda n: n[1], reverse=True)
            print(result[0])

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
