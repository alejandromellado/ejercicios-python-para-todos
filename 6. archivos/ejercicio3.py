# Ejercicio 3: Algunas veces cuando los programadores se aburren o
# quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
# a su programa. Modifica el programa que pregunta al usuario por el
# nombre de archivo para que imprima un mensaje divertido cuando el
# usuario escriba “na na boo boo” como nombre de archivo. El programa
# debería funcionar normalmente para cualquier archivo que exista o no
# exista. Aquí está un ejemplo de la ejecución del programa:

def main():
    filename = input('Ingresa un nombre de archivo: ')
    if filename == 'na na boo boo':
        print('NA NA BOO BOO PARA TI - Te he atrapado!')
        exit(0)
    try:
        number_of_lines = 0
        for line in open(filename):
            if line.startswith('Subject:'):
                number_of_lines += 1
        print(f'Hay {number_of_lines} líneas subject en {filename}')
    except Exception as e:
        print(f'No se puede abrir el archivo: {filename}')
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
