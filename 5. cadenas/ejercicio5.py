# Ejercicio 5: Toma el siguiente código en Python que almacena una ca-
# dena:
# str = 'X-DSPAM-Confidence:0.8475'
# Utiliza find y una parte de la cadena para extraer la porción de la cadena
# después del carácter dos puntos y después utiliza la función float para
# convertir la cadena extraída en un número de punto flotante.

def main():
    text = 'X-DSPAM-Confidence:0.8475'
    start = text.find(':') + 1
    n = float(str[start:])
    print(n)


if __name__ == '__main__':
    main()
