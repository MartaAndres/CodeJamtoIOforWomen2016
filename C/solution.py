T = input()
p = 10**9+7
for i in range(T):
    C,V,L = map(int,raw_input().split())
    a = V % p
    b = (C+V)*V % p
    if L == 1:
        c = a
    elif L == 2:
        c = b
    for k in range(3,L+1):
        c = (C*V*a+V*b)%p
        a = b
        b = c
    print 'Case #'+str(i+1)+":",c
