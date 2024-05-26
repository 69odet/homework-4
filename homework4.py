tuple_immutablevar = (1, 2, 3, 'Hello', 'a')
print(tuple_immutablevar)
#tuple_immutablevar [ 8] = 'b'
#print(tuple_immutablevar)      # ошибка, элементы внутри кортежа неизменяемые
list_immutablevar = [1, 2, 3, 'Hello', 'a']
print(list_immutablevar)
list_immutablevar [3] = 'b'
print(list_immutablevar)