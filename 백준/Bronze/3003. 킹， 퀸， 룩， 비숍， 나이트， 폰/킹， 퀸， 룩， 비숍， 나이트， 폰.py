std = [1, 1, 2, 2, 2, 8]

found = list(map(int, input().split()))

result = [std[i] - found[i] for i in range(6)]

print(*result)
