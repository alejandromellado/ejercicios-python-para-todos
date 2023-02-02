# Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
# puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
# está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

# Puntuación Calificación
# >= 0.9 Sobresaliente
# >= 0.8 Notable
# >= 0.7 Bien
# >= 0.6 Suficiente
# < 0.6 Insuficiente


def main():
    score = 0
    try:
        score = float( input('Introduzca puntuación: ') )
        if not (0 <= score <= 1):
            raise ValueError
    except ValueError:
        print('Puntuación incorrecta')
        exit(1)

    if score >= 0.9:
        print('Sobresaliente')
    elif score >= 0.8:
        print('Notable')
    elif score >= 0.7:
        print('Bien')
    elif score >= 0.6:
        print('Suficiente')
    else:
        print('Insuficiente')


if __name__ == '__main__':
    main()
