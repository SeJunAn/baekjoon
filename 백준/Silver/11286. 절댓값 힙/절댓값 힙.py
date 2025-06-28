import sys
from queue import PriorityQueue

input = sys.stdin.readline
queue = PriorityQueue()

n = int(input())

for i in range(n):
    x = int(input())
    if x != 0:
        queue.put((abs(x), x))
    else:
        if(queue.empty()):
            print("0")
        else:
            print(str(queue.get()[1]))