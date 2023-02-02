# Ejercicio 5: Escribir un programa para leer a través de datos de una ban-
# deja de entrada de correo y cuando encuentres una línea que comience
# con “From”, dividir la línea en palabras utilizando la función split.
# Estamos interesados en quién envió el mensaje, lo cual es la segunda
# palabra en las líneas que comienzan con From.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Tendrás que analizar la línea From e imprimir la segunda palabra de
# cada línea From, después tendrás que contar el número de líneas From
# (no incluir From:) e imprimir el total al final. Este es un buen ejemplo
# de salida con algunas líneas de salida removidas:
# python fromcuenta.py
# Ingresa un nombre de archivo: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# [...líneas de salida removidas...]
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# Hay 27 lineas en el archivo con la palabra From al inicio

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            relevant = [line for line in file if 'From ' in line]
            for line in relevant:
                email = line.split()[1]
                print(email)
            print(f'Hay {len(relevant)} lineas en el archivo con la palabra From al inicio')
    except:
        print(f'No se puede abrir el archivo: {filename}')


if __name__ == '__main__':
    main()
