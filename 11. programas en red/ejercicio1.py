# Ejercicio 1: Cambia el programa del socket socket1.py para que le pida al
# usuario la URL, de modo que pueda leer cualquier página web. Puedes
# usar split('/') para dividir la URL en las partes que la componen, de
# modo que puedas extraer el nombre del host para la llamada a connect
# del socket. Añade comprobación de errores utilizando try y except para
# contemplar la posibilidad de que el usuario introduzca una URL mal
# formada o inexistente.

import socket


def main():
    url = input('URL (ej. www.paginaweb.com/index.html): ')

    try:
        misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        misock.connect((f'{ url.split("/")[0] }', 80))
        cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
        misock.send(cmd)

        while True:
            datos = misock.recv(512)
            if len(datos) < 1:
                break
            print(datos.decode(), end='')

        misock.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

# Código: https://es.py4e.com/code3/socket1.py
