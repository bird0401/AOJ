s=input()
bao,bah,bax,cnt=[],[],[],0
for i in range(10):
    if s[i]=='o':bao+=[str(i)]
    elif s[i]=='?':bah+=[str(i)]
    else:bax+=[str(i)]
    
for i in range(10000):
    si=list(str(i))
    while len(si)<4:
        si.insert(0,"0")
    flag=0
    for e in bao:
        if e not in si:flag=1;break
    if flag==1:continue
    for e in bax:
        if e in si:flag=1;break
    if flag==1:continue
    cnt+=1
        
print(cnt)

# ooo???xxxx
# 012
# 3*2*1*
# 345