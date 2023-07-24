users_list = [
    'sasha', 'vanya', 'masha', 'sasha', 'masha'
]

users_set = {
    'sasha', 'vanya', 'masha', 'sasha', 'masha'
}

users_set2 = {
    'dasha', 'vanya', 'masha', 'masha', 'petro'
}


print(users_list, 'users_list')
print(users_set, 'users_set')
print(users_set.intersection(users_set2), 'intersaction')
print(users_set.union(users_set2), 'uniion')


users_set_from_list = set(users_list)
print(users_set_from_list, 'users_set_from_list')
