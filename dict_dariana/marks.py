marks = {
    'Dumitru': 10,
    'Ion'    : 8,
    'Maria'  : 7
}

marks['Ion']   = 10
marks['Maria'] = 10
marks['Sorin'] = 10

print(marks)

# Verificarea existentei unei kei in dictionar
if 'Ion' in marks:
    print('Cheia exista.')
else:
    print('Cheia nu exista.')


# Utilizez variabila de aceea am scris mark daca nu o utilizam puneam _
# for mark in marks:
#     print(mark)
#     print(marks[mark])

for key, value in marks.items():
    print(key,value)

# print(marks)
# print(type(marks))
# # Accesam elementele din dictionar
# print(marks['Dumitru'])
# print(marks['Maria'])
# # Adaugam un element in dictionar
# marks['Andre'] = 9


user = {
    'name': 'Alex',
    'age': 25
}

user['email'] = 'alex@email.com'

print(user)

