# n = int(input())

# choices = []

# for p in range(1,n):
#     k = pow(n,1/p)
#     choices.append(k+p)

# k相对较小，所以我们应该枚举k而不是p

# for k in range(1,n):
#     p = pow(n,1/k)    
#     choices.append(p + k)

# print(int(max(choices)))

# 不好意思，还是过于复杂

#试着分析数学关系，p**k = n,则logp(n) + p == max  求导可知在p>1时候，单增，则使p最大，则k=1

# 所以
a = int(input())
print(a+1)