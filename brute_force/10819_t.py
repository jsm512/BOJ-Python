n = int(input())
arr = list(map(int,input().split()))

ans = []
order = []

def solve(depth):
    if depth == n:
        ans.append(
            sum(abs(arr[order[i+1]] - arr[order[i]]) for i in range(n-1)))
        
        return
    for x in range(n):
        if x not in order:
            order.append(x)
            solve(depth + 1)
            order.pop()
solve(0)
print(max(ans))