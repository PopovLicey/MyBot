n = int(input())
first = 0
second = 1
for i in range(2, n):
    third = first
    first = second
    second = third + first
print(second)