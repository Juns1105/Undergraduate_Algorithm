
# price is dict of revenue we get for the corresponding rod-length
price={1:1,2:5,3:8,4:9,5:10,6:17,7:17,8:20,9:24,10:30}

def cut_rod(n,price):
    if n==0:
        return 0
    revenue=-9999
    for i in range(1,n+1):
        revenue=max(revenue,price[i]+cut_rod(n-i,price))
    return revenue

for i in range(1,11):
    n=i # print the maximum revenue we earn for rod of length i
    revenue=cut_rod(n,price)
    print "revenue for rod of length %d is %d" %(n,revenue)
