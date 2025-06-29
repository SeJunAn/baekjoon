import sys

input = sys.stdin.readline

a = list(map(int, input().strip()))

for i in range(len(a) - 1):
    Max = i
    for j in range(i + 1, len(a)):
        if a[j] > a[Max]:
            Max = j
    if a[i] < a[Max]:
        temp = a[i]
        a[i] = a[Max]
        a[Max] = temp
    
print(''.join(map(str, a)))