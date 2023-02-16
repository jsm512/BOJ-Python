arr = []
for i in range(9):
    arr.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            n,p = i,j
            break

new_arr=[]
for i in range(len(arr)):
    if i == n or i == p:
        continue
    new_arr.append(arr[i])
new_arr.sort()
for i in range(len(new_arr)):
    print(new_arr[i])