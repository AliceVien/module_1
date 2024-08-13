my_dict = {'Name' : 'Kutya', 'age' : '23', 'intelligence' : 'average'}
print(my_dict)
print(my_dict.get('Name'))
print(my_dict.get('Kukutya'))
my_dict.update({'mood' : 'excellent', 'her phone number' : 89267698176})
print(my_dict.pop('her phone number'))
print(my_dict)

my_set =  {1, 2, 3, 4, 5, 'вышел зайчик погулять', 5, 4, 3, 2, 1, (5, 4, 3, 2, 1)}
print(my_set)
new_elements = ['вдруг охотник выбегает', 10101010]
my_set.update(new_elements)
my_set.remove(10101010)
print(my_set)