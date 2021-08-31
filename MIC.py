s=input()
bao,bax,cnt=[],[],0
for i in range(10):
    if s[i]=='o':bao+=[str(i)]
    elif s[i]=='x':bax+=[str(i)]

for i in range(10000):
    si=f'{i:04}'
    if any(e not in si for e in bao) or any(e in si for e in bax):continue
    cnt+=1
        
print(cnt)