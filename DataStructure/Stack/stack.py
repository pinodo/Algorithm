# Stack: Last-in-first-out (LIFO)
stack = []

stack.append(7)  # 7
stack.append(2)  # 7 - 2
stack.append(5)  # 7 - 2 - 5
stack.pop()      # 7 - 2
stack.append(1)  # 7 - 2 - 1
stack.append(4)  # 7 - 2 - 1 - 4
stack.append(3)  # 7 - 2 - 1 - 4 - 3
stack.append(9)  # 7 - 2 - 1 - 4 - 3 - 9
stack.pop()      # 7 - 2 - 1 - 4 - 3

print(stack[::-1])  # from the upper element to the lower
print(stack)  # from the lower element to the upper
