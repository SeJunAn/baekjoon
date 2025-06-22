import sys

input = sys.stdin.readline

size, cnt = map(int, input().split())

# 입력 배열
arr = list(map(int, input().split()))
arr.insert(0, 0)

sum_arr = [0, arr[1]]
for i in range(2, size + 1):
    sum_arr.append(sum_arr[i - 1] + arr[i])

for i in range(cnt):
    start_idx, end_indx = map(int, input().split())
    print(sum_arr[end_indx] - sum_arr[start_idx - 1])