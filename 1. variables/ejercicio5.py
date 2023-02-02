# Ejercicio 5: Escribe un programa que le pida al usuario una temper-
# atura en grados Celsius, la convierta a grados Fahrenheit e imprima
# por pantalla la temperatura convertida.

def main():
    text = input('Introduzca temperatura en grados Celsius: ')
    celc = float(text)
    fahr = (celc * 1.8) + 32
    print(f'Temperatura en grados Fahrenheit: {fahr}')


if __name__ == '__main__':
    main()
