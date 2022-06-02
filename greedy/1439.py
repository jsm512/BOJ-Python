s = input()

# zero_str=s.split('1')
# first_str = s.split('0')

# zero_cnt=0
# first_cnt=0
# for i in zero_str:
#     if i != '':
#         zero_cnt+=1
# for i in first_str:
#     if i != '':
#         first_cnt+=1
# print(min(zero_cnt,first_cnt))

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt+=1
print((cnt+1)//2)
