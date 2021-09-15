def longest_substring(str1,str2,m,n,count):
    if m==0 or n==0:
       return 0
    else:
       if str1[m-1]==str2[n-1]:
          count=longest_substring(str1,str2,m-1,n-1,count+1)
          return count
       else:
          count=max(max(longest_substring(str1,str2,m-1,n,0),longest_substring(str1,str2,m,n-1,0)),count)
          return count

def l_substring(str1,str2,m,n,count):
    T=[[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
      for j in range(n+1):
         if i==0 or j==0:
             T[i][j]=0
    for i in range(1,m+1):
      for j in range(1,n+1):
          if str1[i-1]==str2[j-1]:
             T[i][j]=1+T[i-1][j-1]
             if count<T[i][j]:
                count=T[i][j]
          else:
             T[i][j]=0
             if count<T[i][j]:
                count=T[i][j]
    return count

if __name__=="__main__":
   print(longest_substring("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB"),0))
   print(l_substring("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB"),0))
   