# Ejercicio 5: Este programa almacena el nombre del dominio (en vez de
# la dirección) desde donde fue enviado el mensaje en vez de quién envió
# el mensaje (es decir, la dirección de correo electrónica completa). Al
# final del programa, imprime el contenido de tu diccionario.
# python schoolcount.py
# Ingresa un nombre de archivo: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            relevant_lines = [line for line in file if 'From ' in line]

            counter = {}
            for line in relevant_lines:
                sender = line.split()[1]
                domain = sender.split(sep='@')[1]
                counter[domain] = 1 if (domain not in counter) else (counter[domain] + 1)

            print(counter)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
