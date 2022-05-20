import sys


i = 1
while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if sum(arr) == 0:
        break
    ans = (arr[2]//arr[1])*arr[0]
    ans += min(arr[0],(arr[2]%arr[1]))
    print(f'Case {i}: {ans}')
    i+=1