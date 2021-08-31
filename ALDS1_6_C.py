inf=10**20
def merge(l,left,mid,right):
    fo,ba,i,j=l[left:mid]+[[inf,inf]],l[mid:right]+[[inf,inf]],0,0
    for k in range(left,right):
        if fo[i][1]<=ba[j][1]:l[k]=fo[i];i+=1
        else:l[k]=ba[j];j+=1
def mergesort(l,left,right):
    if right-left>1:
        mid=(left+right)//2
        mergesort(l,left,mid)
        mergesort(l,mid,right)
        merge(l,left,mid,right)

def partition(l,p,r):
    pi=l[r][1]
    j=p-1
    for i in range(p,r):
        if l[i][1]<=pi:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[r],l[j]=l[j],l[r]
    return j
def quicksort(l,p,r):
    if p<r:
        q=partition(l,p,r)
        quicksort(l,p,q-1)
        quicksort(l,q+1,r)

n=int(input())
a,b=[],[]
for i in range(n):
    e1,e2=input().split()
    a+=[[e1,int(e2)]]
    b+=[[e1,int(e2)]]
quicksort(a,0,n-1)
mergesort(b,0,n)
print("Stable" if a==b else "Not stable")
for e in a:
    print(*e)