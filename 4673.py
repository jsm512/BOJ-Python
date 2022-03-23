def d(n):
    sum = n
    while (n!=0):
        sum+=n%10
        n//=10
    return sum
check_list=[True]*10001
for i in range(1,10001):
    n=d(i)
    if(n<10001):
        check_list[n]=False
for i in range(1,10001):
    if(check_list[i] == True):
        print(i)