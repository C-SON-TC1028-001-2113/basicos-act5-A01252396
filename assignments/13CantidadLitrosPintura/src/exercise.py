import math
def main():
    #escribe tu código abajo de esta línea
    AreaPintar=float(input('Area a pintar en metros: '))
    LitroPintura=float(input('Rendimiento (m2/l): '))

    LitrosNecesarios=AreaPintar/LitroPintura
    print("Litros a comprar: " + str(int(math.ceil(AreaPintar/LitroPintura))))
if __name__ == '__main__':
    main()
