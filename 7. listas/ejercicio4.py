# Ejercicio 4: Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
# Escribir un programa para abrir el archivo romeo.txt y leerlo línea
# por línea. Para cada línea, dividir la línea en una lista de palabras
# utilizando la función split. Para cada palabra, revisar si la palabra ya
# se encuentra previamente en la lista. Si la palabra no está en la lista,
# agregarla a la lista. Cuando el programa termine, ordenar e imprimir
# las palabras resultantes en orden alfabético.
# Ingresar nombre de archivo: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

def main():
    filename = input('Ingresar nombre de archivo: ')
    try:
        with open(filename) as file:
            unique_words = []
            for line in file:
                for word in line.split():
                    if word not in unique_words:
                        unique_words.append(word)
            print(sorted(unique_words))
    except:
        print(f'No se puede abrir el archivo: {filename}')


if __name__ == '__main__':
    main()
