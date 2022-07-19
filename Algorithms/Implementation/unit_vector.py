# simulation & total search -> Using unit vector

# [E, N, W, S]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# current location
x, y = 2, 2

for i in range(4):
    # next location
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
