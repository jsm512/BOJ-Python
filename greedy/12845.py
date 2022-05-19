import sys


n = int(input())
level = list(map(int,sys.stdin.readline().split()))

max_level = max(level)
idx = level.index(max_level)
max_gold = 0
del level[idx]
max_gold = sum(level) + max_level*len(level)
print(max_gold)
