h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
inf=10**20
dp=[[-inf]*w for _ in range(h)]
dp[-1][-1]=0
dic={"+":1,"-":-1}
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if i+1<h:dp[i][j]=max(dp[i][j],-dp[i+1][j]+dic[c[i+1][j]])
        if j+1<w:dp[i][j]=max(dp[i][j],-dp[i][j+1]+dic[c[i][j+1]])

print(*dp,sep="\n")
if dp[0][0]>0:print("Takahashi")
elif dp[0][0]==0:print("Draw")
else:print("Aoki")


