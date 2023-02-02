# Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo
# dependiendo del día de la semana en que se recibió. Para hacer esto
# busca las líneas que comienzan con “From”, después busca por la tercer
# palabra y mantén un contador para cada uno de los días de la semana.
# Al final del programa imprime los contenidos de tu diccionario (el orden
# no importa).
# Línea de ejemplo:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Ejemplo de ejecución:
# python dow.py
# Ingresa un nombre de archivo: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            relevant_lines = [line for line in file if 'From ' in line]

            day_counter = {}
            for line in relevant_lines:
                day = line.split()[2]
                day_counter[day] = 1 if (day not in day_counter) else (day_counter[day] + 1)

            print(day_counter)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
