# Given a N x N space, a traveler A can move to U(Up), D(Down), R(Right), L(Left) by one space
# An out of range movement will be ignored

# Input Example
# 5
# R R R U D D

# Output Example
# 3 4

# my answer
def fun():
    movements = int(input('Movements: '))
    schedule = list(map(str, input('Keys: ').strip().split()))
    # R U L D
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = 1, 1
    # print(schedule)
    if 1 < movements <= 100 and 1 <= len(schedule) <= 100:
        for i in range(movements):
            if schedule[i] == 'R':
                nx, ny = x + dx[0], y + dy[0]
            elif schedule[i] == 'U':
                nx, ny = x + dx[1], y + dy[1]
            elif schedule[i] == 'L':
                nx, ny = x + dx[2], y + dy[2]
            elif schedule[i] == 'D':
                nx, ny = x + dx[3], y + dy[3]
        return nx, ny


# ex answer
def fun2():
    n = int(input('Movements: '))
    x, y = 1, 1
    plans = input('Plans: ').split()
    print(plans)

    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, 1, -1]
    # x: ROW, y: COL
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    print(x, y)

fun2()
