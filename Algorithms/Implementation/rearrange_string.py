# Input: Upper Character + Number(0 ~ 9)
# Output: Ascending alphabet order, then sum up the ints

# Example
# Input: K1KA5CB7
# Output: ABCKK13

# Idea
# Sort to String and Integer

# Answer
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
