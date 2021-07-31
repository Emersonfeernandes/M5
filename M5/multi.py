"""
Função que calcula e retorna strings.
"""
def num_multi(var):
    """
    Função unica da aplicação.
    """
    if var%5 == 0 and var%7 == 0:
        return 'fizzbuzz'
    elif var%5 == 0:
        return 'fizz'
    elif var%7 == 0:
        return 'buzz'
    else:
        return 'miss'
