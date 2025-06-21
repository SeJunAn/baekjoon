request = int(input())
temp = []

for i in range(request):
    temp.append(int(input()))

temp.sort()
for i in range(request):
    print(temp[i])