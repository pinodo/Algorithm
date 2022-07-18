list_temp = ['a', 'b', 'c', 'd', 'e']


def remove_specific_item() -> list:
    list_temp.remove('b')
    return list_temp


def remove_specific_index():
    list_temp.pop(1)
    return list_temp


def remove_last_index():
    list_temp.pop()
    return list_temp


def sum_list():
    return sum(list_temp)


print('default array         :', "['a', 'b', 'c', 'd', 'e']")
print("remove('b')           :", remove_specific_item())
list_temp = ['a', 'b', 'c', 'd', 'e']
print('remove(1)             :', remove_specific_index())
list_temp = ['a', 'b', 'c', 'd', 'e']
print('pop()                 :', remove_last_index())
list_temp = [0, 1, 2, 3, 4]
print('sum() [0, 1, 2, 3, 4] :', sum_list()) # list / tuple / array
print('[:3]                  :', list_temp[:3])
print('[2:4]                 :', list_temp[2:4])
print('[2:]                  :', list_temp[2:])