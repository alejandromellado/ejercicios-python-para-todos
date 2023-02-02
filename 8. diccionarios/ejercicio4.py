# Ejercicio 4: Agrega código al programa anterior para determinar quién
# tiene la mayoría de mensajes en el archivo. Después de que todos los
# datos hayan sido leídos y el diccionario haya sido creado, mira a través
# del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máx-
# imos y mínimos) para encontrar quién tiene la mayoría de mensajes e
# imprimir cuántos mensajes tiene esa persona.

# Ingresa un nombre de archivo: mbox-short.txt
# cwen@iupui.edu 5
# Ingresa un nombre de archivo: mbox.txt
# zqian@umich.edu 195

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            relevant_lines = [line for line in file if 'From ' in line]

            counter = {}
            for line in relevant_lines:
                sender = line.split()[1]
                counter[sender] = 1 if (sender not in counter) else (counter[sender] + 1)

            max_key = max(counter, key=counter.get)
            print(f'{max_key} {counter[max_key]}')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
