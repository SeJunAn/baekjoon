import sys

input = sys.stdin.readline

month = int(input().strip())
day = int(input().strip())

if month == 2:
    if day == 18:
        print("Special")
    elif day > 18:
        print("After")
    else:
        print("Before")

elif month > 2:
    print("After")
else:
    print("Before")