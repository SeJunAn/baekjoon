import sys

input = sys.stdin.readline

n = int(input().strip())
a = []
result = []
max = 0

for i in range(n):
    a.append((int(input().strip()), i))

sorted_a = sorted(a)

for i in range(n):
    if max < sorted_a[i][1] - i:
        max = sorted_a[i][1] - i

print(max + 1)