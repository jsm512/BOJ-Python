n = input()
nl = list(n)
ans = ''
if '0' not in nl:
    print(-1)
else:
    nl.sort(reverse=True)
    for i in nl:
        ans += i
    if int(ans) % 30 == 0:
        print(int(ans))
    else:
        print(-1)