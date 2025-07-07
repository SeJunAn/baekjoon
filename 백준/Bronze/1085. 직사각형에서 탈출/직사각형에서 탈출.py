import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().strip().split())

print(min(abs(w-x), abs(x-0), abs(h-y), abs(y-0)))