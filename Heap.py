import random

def Maxheapify(a): # only care about node which has a child
    i=(len(a)//2)-1
    max=len(a)
    while i>=0:
        sift_down(a,i,max)
        i-=1

def switch(a,i,j):
    a[i],a[j]=a[j],a[i]

def sift_down(a,i,max):
    while True:
        paridx=i #parent index
        l=2*i+1 #left-child
        r=2*i+2 #right-child

        for k in [l,r]:
            if k<max and a[k]>a[paridx]: #if node has a child and bigger than child
                paridx=k
        if paridx==i:#if parent index is biggest among the key, out from the loop
            return
        switch(a,i,paridx)#switch between parent and child
        i=paridx

def insert(a):
    num=input('press value what you want to insert:')
    b=a.append(num)
    return b

def dele(a):
    num=input('press value what you want to delete:')
    b=a.remove(num)
    return b

def search(a):
    num=input('press index what you want to search')
    b=a[num-1:]
    return b

num=input('range of data:')
i=input('length of tree:')
a=random.sample(range(num),i)#create random list(array)

print a  # Show generated list(tree) first.
save=a
Maxheapify(a)
print a
add=input('If you want add more data, press 1 if not press other number.')
remo=input('If you want delete data, press 1 if not press other number.')
srch=input('If you want search data, press 1 if not press other number.')

while add==1 or remo==1 or srch==1:

    if srch==1:
        b=search(save)
    else:
        pass

    if add==1:
        insert(a)
    else :
        pass

    if remo==1:
        dele(a)
    else:
        pass

    print a
    Maxheapify(a)
    print('this is heapified list')
    print a
    print('this is searched list')
    print b
    Maxheapify(b)
    print('this is heapified searching list')
    print b


    add=input('If you want add more data, press 1 if not press other number.')
    remo=input('If you want delete more data, press 1 if not press other number.')
    srch=input('If you want search data, press 1 if not press other number.')
