# Ejercicio 1: Escribe un programa que lea un archivo e imprima su con-
# tenido (línea por línea), todo en mayúsculas. Al ejecutar el programa,
# debería parecerse a esto:
# python shout.py
# Ingresa un nombre de archivo: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500
# Puedes descargar el archivo desde www.py4e.com/code3/mbox-short.txt

def main():
    filename = input('Ingresa un nombre de archivo: ')
    try:
        file = open(filename)
        for line in file:
            print(line.rstrip().upper())
    except:
        print(f'No se puede abrir el archivo: {filename}')
        exit(1)


if __name__ == '__main__':
    main()
