cnt = int(input())

score = list(map(int, input().split()))

max_score = max(score)

new_score_sum = 0

for i in range(cnt):
    new_score_sum += score[i] / max_score * 100

print(new_score_sum / cnt)