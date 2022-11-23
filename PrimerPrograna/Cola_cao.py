
print('me voy a la cocina')
print('abro la nevera')

hay_leche = input('¿Hay leche? (S/N) ')
hay_colacao = input('¿Hay colacao? (S/N) ')

if hay_leche == 'S' or hay_colacao != 'S':
    print('Voy al super')
    if hay_leche != 'S':
        print('Voy a comprar leche')
    if hay_colacao != 'S':
        print('Voy a comprar colacao')


