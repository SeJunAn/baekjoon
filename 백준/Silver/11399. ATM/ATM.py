import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().strip().split()))

for i in range(1, len(a)):
    target = a[i]
    target_point = i
    for j in range(i - 1, -1, -1):
        if a[j] < a[i]:
            target_point = j + 1
            break
        if j == 0:
            target_point = 0
    
    for j in range(i, target_point, -1):
        a[j] = a[j - 1]
    
    a[target_point] = target


s = []
temp = 0

for i in range(len(a)):
    temp += a[i]
    s.append(temp)

print(sum(s))