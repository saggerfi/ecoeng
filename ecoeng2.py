class Menu:
    
    def __init__(self, concepto):
        self.concepto = concepto
    

    def despliega(self, referencia):
        return f'{concepto} en función del {referencia}'


def costo_inicial():
    ci = Menu('')


def valor_salvamento():
    pass


def prestamo():
    pass


def ingreso():
    pass


def egreso():
    pass


def main():

    fedi = """
    RESOLUCIÓN DE FEDI
    ¿Qué quieres determinar?

    1- Costo Inicial
    2- Valor de Salvamento
    3- Préstamo
    4- Ingreso
    5- Egreso 

    Respuesta: """

    respuesta = int(input(fedi))
    if respuesta == 1:
        costo_inicial()
    elif respuesta == 2:
        valor_salvamento()
    elif respuesta == 3:
        prestamo()
    elif respuesta == 4:
        ingreso()
    elif respuesta == 5:
        egreso()


if __name__ == '__main__':
    main()