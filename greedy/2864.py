a,b = input().split()
arr = []
arr.append(int(a.replace('6','5')) + int(b.replace('6','5')))
arr.append(int(a.replace('5','6')) + int(b.replace('5','6')))
print(min(arr), max(arr))