def lcs(str1,str2,m,n):
   T=[[-1 for i in range(n+1)] for j in range(m+1)]
   for i in range(m+1):
      for j in range(n+1):
        if i==0 or j==0:
           T[i][j]=0
   for i in range(1,m+1):
     for j in range(1,n+1):
          if str1[i-1]==str2[j-1]:
             T[i][j]=1+T[i-1][j-1]
          else:
             T[i][j]=max(T[i][j-1],T[i-1][j])
   return T

def print_lcs(str1,str2,m,n):
    T=lcs(str1,str2,m,n)
    temp_str=""
    i=m
    j=n
    while i>0 and j>0:
       if str1[i-1]==str2[j-1]:
          temp_str+=str1[i-1]
          i=i-1
          j=j-1
       elif T[i][j-1]>T[i-1][j]:
            j=j-1
       else:
            i=i-1
    return temp_str

            
if __name__=="__main__":
   print(lcs("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))
   print(print_lcs("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))