# Ejercicio 7: Reescribe el programa de calificaciones del capítulo ante-
# rior usando una función llamada calcula_calificacion, que reciba una
# puntuación como parámetro y devuelva una calificación como cadena.

def calcula_calificacion(score):
    if score >= 0.9:
        return 'Sobresaliente'
    if score >= 0.8:
        return 'Notable'
    if score >= 0.7:
        return 'Bien'
    if score >= 0.6:
        return 'Suficiente'

    return 'Insuficiente'


def main():
    score = 0
    try:
        score = float( input('Introduzca puntuación: ') )
        if not (0 <= score <= 1):
            raise ValueError
    except ValueError:
        print('Puntuación incorrecta')
        exit(1)

    print(calcula_calificacion(score))


if __name__ == '__main__':
    main()

