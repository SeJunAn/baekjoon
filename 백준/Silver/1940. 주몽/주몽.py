import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [int(x) for x in input().strip().split()]
arr.sort()

i = 0
j = n - 1
count = 0

while(i < j):
    if(arr[i] + arr[j] > m):
        j -= 1
    
    elif(arr[i] + arr[j] == m):
        count += 1
        i += 1
        j -= 1

    else:
        i += 1

print(count)