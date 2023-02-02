# Ejercicio 1: Escribe un programa que lea repetidamente números hasta
# que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números. Si el usuario introduce cualquier otra cosa que no sea un
# número, detecta su fallo usando try y except, muestra un mensaje de
# error y pasa al número siguiente.

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

    total = sum(numbers)
    entries = len(numbers)
    print(f'{total} {entries} {total / entries}')


if __name__ == '__main__':
    main()
