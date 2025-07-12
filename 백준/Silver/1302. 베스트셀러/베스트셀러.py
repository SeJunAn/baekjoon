# 입력 받기
n = int(input())
book_counts = {}

# 책 제목 개수 세기
for _ in range(n):
    title = input().strip()
    if title in book_counts:
        book_counts[title] += 1
    else:
        book_counts[title] = 1

# 가장 많이 팔린 수 찾기
max_count = max(book_counts.values())

# 가장 많이 팔린 책들만 추리기
most_sold_books = []
for title in book_counts:
    if book_counts[title] == max_count:
        most_sold_books.append(title)

# 사전 순으로 가장 앞서는 제목 출력
most_sold_books.sort()
print(most_sold_books[0])
