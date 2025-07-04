import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

a.sort()

print(a[k-1])