import math as ma
op = 0
italiana = 1000
hawaiana = 2000
americana = 3000
chilena = 5000
total_pizza = 0
cant_ame = 0
cant_chi = 0
cant_haw = 0
cant_ita = 0
print('me indica su nombre?')
nombre = str(input(': '))
while op != 5:
    try:
        print(
            f'\t--->pizza<---\n que pizza desea: \n1. italiana =${italiana}\n2. hawaiana =${hawaiana}\n3. americana =${americana}\n4. chilena =${chilena}\n salir')
        op = int(input(': '))
        if op == 1:
            print('cuantas desea: ')
            cantidad = int(input(': '))
            cant_ita = cantidad * italiana
        if op == 2:
            print('cuantas desea: ')
            cantidad = int(input(': '))
            cant_haw = cantidad * hawaiana
        if op == 3:
            print('cuantas desea: ')
            cantidad = int(input(': '))
            cant_ame = cantidad * americana
        if op == 4:
            print('cuantas desea: ')
            cantidad = int(input(': '))
            cant_chi = cantidad * chilena
    except ValueError:
        print('tiene que ser un numero')

    total_pizza = cant_ame + cant_haw + cant_ita + cant_chi

opcion = 0
agregado = 0
while opcion != 1:
    try:
        print('quiere agregar un agregado?\n1. si\n2. no')
        opcion = int(input(': '))
        if opcion == 1:
            bebida = 2000
            papas_fritas = 1500
            nuggets = 1000
            print(
                f'que agregado quiere?\n1. bebida ${bebida}\n2. papas fritas ${papas_fritas}\n3. nuggets ${nuggets}')
            agregado = int(input(': '))
            if agregado == 1:
                agregado = bebida
            if agregado == 2:
                agregado = papas_fritas
            if agregado == 3:
                agregado = nuggets
    except ValueError:
        print('tiene que ser un numero')
op_envio = 0
while op_envio != 2:
    try:
        print('desea envio ? si tiene el valor es mayor a $10000 es gratis si no tiene un costo del 15% \n1. si\n 2. no ')
        op_envio = int(input(': '))
        if op_envio == 1:
            if (total_pizza + agregado) >= 10000:
                envio = 0
                total_envio = (total_pizza + agregado + envio)
            else:
                envio = ma.ceil(total_pizza + agregado) * 0.15
                total_envio = total_pizza + envio
            print(' ---> pizza <---')
            print(f'retiro a nombre de :{nombre}')
            print(f'italiana ${cant_ita}')
            print(f'hawaiana ${cant_haw}')
            print(f'chilena ${cant_chi}')
            print(f'americana ${cant_ame}')
            print(f'agregado ${agregado}')
            print(f'envio : ${envio}')
            print(f'total a pagar: $ {total_envio}')

            print('muchas gracias, vuelva pronto')

        else:
            envio = 0
            print(' ---> pizza <---')
            print(f'retiro a nombre de :{nombre}')
            print(f'italiana ${cant_ita}')
            print(f'hawaiana ${cant_haw}')
            print(f'chilena ${cant_chi}')
            print(f'americana ${cant_ame}')
            print(f'agregado ${agregado}')
            print(f'dando un total de : ${total_pizza}')
            print('muchas gracias, vuelva pronto')
    except ValueError:
        print('tiene que ser un numero ')
    break
