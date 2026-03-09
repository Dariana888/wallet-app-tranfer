lista_cumparaturi = ['paine', 'lapte', 'covrigi']

print(f'Lista originala:  {lista_cumparaturi}')
lista_cumparaturi[0] = 'paine cu toast'
print(f'Lista modificata: {lista_cumparaturi}')

# adaugam doua produse noi
lista_cumparaturi.append('oua')
lista_cumparaturi.append('salam')

print(lista_cumparaturi)