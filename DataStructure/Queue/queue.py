# Queue: First-in-first-out (FIFO)
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(8)
queue.popleft()
queue.append(4)
queue.append(9)
queue.popleft()

print(queue)  # Order: From the first one
queue.reverse()
print(queue)  # Order: From the last one
