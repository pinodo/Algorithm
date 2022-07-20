# In a chess board(8x8), knight can only move as L form
# 1. two horizontal movements, then one vertical movement
# 2. two vertical movements, then one horizontal movement
# Given the knight position, write a code that calculates the all possible movements
# row: 1 - 8, col: a - h

# Input Example
# a1

# Output Example
# 2


# my answer
def knight_movements():
    crt_location = list(input('Enter the current location: '))
    char_sets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # print(crt_location)
    col = char_sets.index(crt_location[0]) + 1
    row = int(crt_location[1])
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    types = ['LLU', 'LUU', 'RUU', 'RRU', 'RRD', 'RDD', 'LDD', 'LLD']
    result = 0
    for i in range(len(types)):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 1 or ny < 1:
            continue
        result += 1
    return result


print(knight_movements())


# ex answer
def knight_movements2():
    input_data = input('Enter the current location: ')
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1
    return result


print(knight_movements2())