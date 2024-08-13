immutable_var = 8, 800, 555, 35, 35, 'Проще позвонить, чем у кого-то занимать!', True
print(immutable_var)
#Кортежи (tuple) являются неизменяемыми последовательностями, что означает, что после их создания их нельзя модифицировать.
#Это свойство отличается от списков (list).
mutable_list = ['реклама:', 8, 800, 555, 35, 35, 'Проще позвонить, чем у кого-то занимать!']
print(mutable_list)
mutable_list.remove('реклама:')
mutable_list[0] = '+7'
mutable_list.append(True)
mutable_list.extend('ЗВОНИ')
mutable_list.extend(['БЫСТРЕЕ', 2])
print(mutable_list)
