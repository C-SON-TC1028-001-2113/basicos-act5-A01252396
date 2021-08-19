import math
def main():
    #escribe tu código abajo de esta línea
    Altura=int(input('Altura de la casa: '))
    Angulo=int(input('Angulo en grados: '))
    Largo=round(Altura/math.sin(math.radians(Angulo)))
    print("Largo de la escalera: " + str(Largo))

if __name__ == '__main__':
    main()
