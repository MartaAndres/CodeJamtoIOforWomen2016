t = input()
for i in range(t):
    n = input()
    a = map(int,raw_input().split())
    sol = []
    while a:
        sol.append(a[0])
        a.remove(a[0]*4/3)
        a = a[1:]
    print 'Case #'+str(i+1)+": " + ' '.join(map(str,sol))
