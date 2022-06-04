import sys


n,m = map(int,sys.stdin.readline().split())

bundle=[]
piece = []

for _ in range(m):
    a,b = map(int,input().split())
    bundle.append(a)
    piece.append(b)
min_cost_bundle=min(bundle)
min_cost_piece=min(piece)

if min_cost_bundle < min_cost_piece * 6:
    if min_cost_bundle < (n%6)*min_cost_piece:
        print((n//6)*min_cost_bundle+min_cost_bundle)
    else:
        print((n//6)*min_cost_bundle + (n%6)*min_cost_piece)
elif min_cost_bundle >= min_cost_piece*6:
    print(n*min_cost_piece)