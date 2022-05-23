my_input = input().split('-')

arr=[]

for i in my_input:
    my_sum = 0
    my_str=i.split('+')
    for j in my_str:
        my_sum+=int(j)
    arr.append(my_sum)
n = arr[0]
for i in range(1,len(arr)):
    n-=arr[i]
print(n)



