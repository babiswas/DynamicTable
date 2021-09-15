def longest_common_subsequence(str1,str2,m,n,T):
    if m==0 or n==0:
       return 0
    if T[m][n]!=-1:
       return T[m][n]
    else:
       if str1[m-1]==str2[n-1]:
          T[m][n]=1+longest_common_subsequence(str1,str2,m-1,n-1,T)
       else:
          T[m][n]=max(longest_common_subsequence(str1,str2,m-1,n,T),longest_common_subsequence(str1,str2,m,n-1,T))
       return T[m][n]


def lcs(str1,str2,m,n):
    T=[[-1 for i in range(n+1)] for j in range(m+1)]
    return longest_common_subsequence(str1,str2,m,n,T)


if __name__=="__main__":
   print(lcs("AGGTAB","GXTXAYB",len("AGGTAB"),len("GXTXAYB")))
 
