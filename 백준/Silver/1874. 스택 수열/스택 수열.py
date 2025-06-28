import sys

input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    su = a[i]
    if su >= num:
        while(su >= num):
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
            
    else:
        temp = stack.pop()
        if temp > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)
