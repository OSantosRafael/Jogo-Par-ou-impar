from random import randint
print('Vamos jogar Par ou Impar')
cont = 0
while True:
    escolha = str(input('Par ou Impar? ')).strip().lower()
    while escolha not in 'par' and escolha not in 'impar':
        escolha = str(input('Par ou Impar? ')).strip().lower()
    n = int(input('Digite um número: '))
    c = randint(1, 11)
    r = n + c
    print(f'Resultado: {r}', end=' - ')
    print('Par!' if r % 2 == 0 else 'Impar!')
    if escolha == 'par':
        if r % 2 == 0:
            cont += 1
            print('Você venceu! Jogue novamente!')
        else:
            print('Você perdeu!')
            break
    if escolha == 'impar':
        if r % 2 != 0:
            cont += 1
            print('Você venceu! Jogue novamente.')
        else:
            print('Você perdeu!')
            break
print(f'Vitórias consecutivas: {cont}')
