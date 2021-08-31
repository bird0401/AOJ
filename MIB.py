n=int(input())
ab=[]
for _ in range(n):
    e1,e2=input().split()
    ab+=[[e1,int(e2)]]
ab.sort(reverse=True,key=lambda t:t[1])
print(ab[1][0])
