"""
programa principal.
"""
from multi import num_multi


def run():

    """Aplicação do programa."""
    while True:
        num = int(input('Digite um número natural: '))
        if num < 0:
            print('Por favor digite um número natural!')

        else:
            print(num_multi(num))
            break

run()
