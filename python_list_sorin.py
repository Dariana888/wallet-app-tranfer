lista_cumparaturi = ['paine', 'lapte', 'covrigi']

print(f'Lista originala:  {lista_cumparaturi}')
lista_cumparaturi[0] = 'paine cu toast'
print(f'Lista modificata: {lista_cumparaturi}')

# adaugam doua produse noi
lista_cumparaturi.append('oua')
lista_cumparaturi.append('salam')

print(lista_cumparaturi)

# printarea elementelor listei cu ajutorul buclei for
for cumparatura in lista_cumparaturi:
    print(cumparatura)


##################################
################################
lista_exemplu = ['paine', 'lapte', 'covrigi','paine', 'lapte', 'covrigi','paine', 'lapte', 'covrigi','paine', 'lapte', 'covrigi''paine', 'lapte', 'covrigi''paine', 'lapte', 'covrigi''paine', 'lapte', 'covrigi''paine', 'lapte', 'covrigi''paine', 'lapte', 'covrigi','paine', 'lapte', 'covrigi','paine', 'lapte', 'covrigi']

lista_doi = ['test1', 'test2']
print(lista_exemplu[-1])

print(lista_exemplu.extend(lista_doi))

print(lista_exemplu)