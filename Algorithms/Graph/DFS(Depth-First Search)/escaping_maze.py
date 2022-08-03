# You are stuck in maze, size of (NxM) and try to escape avoiding monsters
# Your location is (1, 1) and the exit is on (N, M) and you can move one container by one container
# 0: the place where the monster exists, 1: the place that you can pass through
# Write a program that calculates the minimal movements (contains both the starting and end point)
# Constraints: 4<= N, M <= 200

# Input Example
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# Output Example
# 10


def escape(n, m):

    return False


input_indicator = input()
info = list(input_indicator.split(' '))
row = int(info[0])
col = int(info[1])
maze = [[0] * col] * row
print(maze)
for i in range(row-1):
    maze[i] = input()
print(maze)