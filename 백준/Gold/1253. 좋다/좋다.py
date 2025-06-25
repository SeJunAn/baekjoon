import sys

input = sys.stdin.readline

n = int(input())

arr = [int(x) for x in input().strip().split()]
arr.sort()

count = 0

for k in range(n):
    i = 0
    j = n - 1
    while(i < j):
        if(arr[i] + arr[j] > arr[k]):
            j -= 1
        elif(arr[i] + arr[j] < arr[k]):
            i += 1
        else:
            if(i != k and j != k):
                count += 1
                break
            elif(i == k):
                i += 1
            else:
                j -= 1

print(count)