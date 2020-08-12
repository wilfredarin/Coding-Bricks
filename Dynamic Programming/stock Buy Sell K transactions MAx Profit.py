#stock Buy Sell K transactions MAx Profit
def stock(l,trans):
    days = len(l)
    a = [[0 for i in range(days) ] for j in range(trans+1)]
    #T[i][j] = t[i][j-1] /price[j]-price[m] and t[i-1][m]
    for i in range(1,trans+1):
        for j in range(1,days):
            no_transaction = a[i][j-1]
            trans = 0
            for m in range(j):
                trans = max(trans,l[j]-l[m]+a[i-1][m])
            a[i][j]=max(no_transaction,trans)
    print(a[-1][-1])
test = int(input())
for i in range(test):
    k = int(input())
    days = int(input())
    l =list(map(int,input().split()))
    stock(l,k)
