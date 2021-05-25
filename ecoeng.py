def costo_inicial():
    
    ci = ('X')
    menu1 = """
    Valor de salvamento en función del Costo Inicial:
    1- Sí
    2- No

    Respuesta: """
    respuesta1 = int(input(menu1))
    if respuesta1 == 1:
        vs = (input('VS: '))
    elif respuesta1 == 2:
        vs = int(input('VS: '))
    
    menu2 = """
    Valor de prestámo en función del Costo Inicial:
    1- Sí
    2- No

    Respuesta: """
    respuesta2 = int(input(menu2))
    if respuesta2 == 1:
        p = (input('P: '))
    elif respuesta2 == 2:
        p = int(input('P: '))
    
    menu3 = """
    Valor de Ingreso en función del Costo Inicial:
    1- Sí
    2- No

    Respuesta: """
    respuesta3 = int(input(menu3))
    if respuesta3 == 1:
        i = (input('Ingreso: '))
    elif respuesta3 == 2:
        i = int(input('Ingreso: '))

    menu4 = """
    Valor de Egreso en función del Costo Inicial:
    1- Sí
    2- No

    Respuesta: """
    respuesta4 = int(input(menu4))
    if respuesta4 == 1:
        e = (input('Egreso: '))
    elif respuesta4 == 2:
        e = int(input('Egreso: '))

    print(f'Valor de salvamento: {vs}, Prestámo: {p}, Ingreso: {i}, Egreso: {e}')


def valor_salvamento():
    vs = ('X')


def prestamo():
    p = ('X')


def ingreso():
    i = ('X')


def egreso():
    e = ('X')

def main():

    fedi = """
    Resolución FEDI
    Qué quieres determinar: 

    1- Costo Inicial
    2- Valor de Salvamento
    3- Préstamo
    4- Ingreso
    5- Egreso 

    Respuesta: """

    opcion1 = int(input(fedi))

    if opcion1 == 1:
        costo_inicial()
    elif opcion1 == 2:
        valor_salvamento()
    elif opcion1 == 3:
        prestamo()
    elif opcion1 == 4:
        ingreso()
    elif opcion1 == 5:
        egreso()
    
    print('Cargando 🙄')


if __name__ == '__main__':
    main()