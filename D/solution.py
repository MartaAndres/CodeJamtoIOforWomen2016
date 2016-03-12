import random
T = input()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(T):
    N = input()
    P = raw_input().split()
    sol = '(IM)POSSIBLE??'
    if min(len(x) for x in P) == 1:
        sol = 'IMPOSSIBLE'
    elif N == 1:
        pos = letters.find(P[0][0])
        # place first letter of password at the end
        sol = letters[pos+1:]+letters[:pos+1]
    else:
        # might be possible
        sol = ''
        global_follows = {}
        for l in letters:
            global_follows[l] = set()
            for p in P:
                for k in range(len(p)-1):
                    global_follows[p[k]].add(p[k+1])

        for j in reversed(range(26)):
            follows = {}
            for l in letters:
                if l not in sol:
                    follows[l] = set()
            for p in P:
                for k in range(len(p)-1):
                    if p[k] not in sol and p[k+1] not in sol:
                        follows[p[k]].add(p[k+1])

            if len([len(x) for x in follows.values() if len(x) >= j]) > 1:
                sol = 'IMPOSSIBLE'
            print follows

            sol += letters[j]

        # if len([len(x) for x in follows.values() if len(x) == 25]) > 1:
        #     sol = 'IMPOSSIBLE'
        # else:
        #     keys = list(sorted(follows.keys(),key=lambda w:-len(follows[w])))
        #     sol = keys[0]
        #     keys = keys[1:]
        #     added = True
        #     while keys and added:
        #         added = False
        #         remove = set()
        #         for k in keys:
        #             if sol[0] not in follows[k]:
        #                 sol = k+sol
        #                 remove.add(k)
        #                 added = True
        #         for k in remove:
        #             keys.remove(k)
        #     if not added:
        #         print 'error'
        #         sol = 'IMPOSSIBLE'




        # P.sort(key=lambda w:(len(w),w))
        # sol = P[0][0]
        # P = P[1:]
        # while P:
        #     pos = letters.find(sol[0])
        #     # place first letter of password at the end
        #     order = letters[pos+1:]+letters[:pos+1]
        #     P.sort(key=lambda w:(order.find(w[1]),w))
        #     p = P[0]
        #     P = P[1:]
        #     if sol.find(p) != -1:
        #         print 'error', p, sol
        #         print P
        #         sol = 'IMPOSSIBLE'
        #         break
        #     if any(x in sol for x in p) and p[-1] != sol[0]:
        #         # word is safe
        #         pass
        #     else:
        #         sol = p[0] + sol
    if sol != 'IMPOSSIBLE':
        sol = ''.join(x for x in letters if x not in sol) + sol
    print 'Case #'+str(i+1)+":",sol
