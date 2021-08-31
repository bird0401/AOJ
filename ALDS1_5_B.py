n=int(input())
a=list(map(int,input().split()))
inf,cnt=10**20,0

def merge(l,left,mid,right):
    fo,ba,i,j=l[left:mid]+[inf],l[mid:right]+[inf],0,0
    global cnt
    for k in range(left,right):
        if fo[i]<=ba[j]:l[k]=fo[i];i+=1
        else:l[k]=ba[j];j+=1
        cnt+=1

def mergesort(l,left,right):
    if right-left>1:
        mid=(left+right)//2
        mergesort(l,left,mid)
        mergesort(l,mid,right)
        merge(l,left,mid,right)

mergesort(a,0,n)
print(*a)
print(cnt)