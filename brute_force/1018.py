W_start=[
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
B_start=[
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]
n,m=map(int,input().split())
chess=[]
my_min = 32
W_cnt = 0
B_cnt = 0
for i in range(n):
    chess.append(input())
for i in range(n-7):
    for j in range(m-7):
        for k in range(8):
            for p in range(8):
                if W_start[k][p] != chess[k+i][p+j]:
                    W_cnt += 1
                elif B_start[k][p] != chess[k+i][p+j]:
                    B_cnt += 1
        my_min = min(my_min,min(W_cnt,B_cnt))
        B_cnt = 0
        W_cnt = 0
print(my_min)