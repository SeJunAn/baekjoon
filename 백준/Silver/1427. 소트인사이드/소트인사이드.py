import sys

input = sys.stdin.readline

temp = input().strip()

arr = sorted(temp, reverse=True)
print(''.join(arr))