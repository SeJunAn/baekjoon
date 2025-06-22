a = int(input())
b = list(map(int, input()))
result = 0

for i in range(a):
    result += b[i]

print(result)