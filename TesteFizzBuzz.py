def FizzBuzz(n1):  # Função sobre numeros divisiveis por 3 e 5
    if n1 % 5 == 0 and n1 % 3 == 0:
        return f'FizzBuzz, {n1} é divisivel por 3 e por 5'

    elif n1 % 3 == 0:
        return f'Fizz, {n1} é divisivel por 3'
    elif n1 % 5 == 0:
        return f'Buzz, {n1} é divisivel por 5'

    else:
        return f'{n1} Não é divisivel nem por 3 e nem por 5'


from random import randint  # função para retornar numeros aleatorios em um determinado range, descrito a baixo

for i in range(100):
    aleatorio = randint(0, 100)
    print(FizzBuzz(aleatorio))
