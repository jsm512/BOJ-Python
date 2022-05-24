import sys


n = int(input())

A_input = list(map(int,sys.stdin.readline().split()))
B_input = list(map(int,sys.stdin.readline().split()))

# A_input.sort()
# B_input.sort(reverse=True)

s = 0

for i in range(n):
    s += min(A_input) * max(B_input)
    A_input.pop(A_input.index(min(A_input)))
    B_input.pop(B_input.index(max(B_input)))
print(s)