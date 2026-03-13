# Dictionarul e gol si il completam

users = []

for _ in range(3):
    user = {}
    user['name'] = input('Introdu numele: ')
    user['age'] = int(input('Introdu varsta: '))
    users.append(user)


print(users)
