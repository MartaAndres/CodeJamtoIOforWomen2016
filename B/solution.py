t = input()
for i in range(t):
    D,K,N = map(int,raw_input().split())
    if K%2 == 1:
        end = (K+N)%D
        left = (end+N)%D+1
        right = (end-2+N)%D+1
    else:
        end = (K-N)%D
        left = (end-N)%D+1
        right = (end-2-N)%D+1
    print 'Case #'+str(i+1)+":",left,right
