pay = int(input())
arr = [500,100,50,10,5,1]
change = 1000 - pay
cnt = 0 # 잔돈의 개수

while True:
    if change == 0:
        break
    for i in arr:
        cnt += change // i
        change = change % i
print(cnt)