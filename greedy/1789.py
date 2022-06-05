s = int(input())

n = 0
i = 1

while True:
    n += i
    if n > s:
        break
    i+=1
print(i-1)
