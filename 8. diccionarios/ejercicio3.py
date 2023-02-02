# Ejercicio 3: Escribe un programa para leer a través de un historial de
# correos, construye un histograma utilizando un diccionario para contar
# cuántos mensajes han llegado de cada dirección de correo electrónico, e
# imprime el diccionario.
# Ingresa un nombre de archivo: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            relevant_lines = [line for line in file if 'From ' in line]

            counter = {}
            for line in relevant_lines:
                sender = line.split()[1]
                counter[sender] = 1 if (sender not in counter) else (counter[sender] + 1)

            print(counter)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
