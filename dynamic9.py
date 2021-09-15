import sys
def subset_sum(arr,n,W):
   T=[[False for i in range(W+1)] for i in range(n+1)]
   for i in range(n+1):
     for j in range(W+1):
       if j==0:
          T[i][j]=True
       elif i==0 and j!=0:
          T[i][j]==False
   for i in range(1,n+1):
     for j in range(1,W+1):
       if i-1>=0:
          if arr[i-1]<=j:
             T[i][j]=T[i-1][j] or T[i-1][j-arr[i-1]]
          elif arr[i-1]>j:
             T[i][j]=T[i-1][j]
   print(T)
   return T


def find_minm_subset_sum_diff(arr,n):
    maxm=-1
    if n==0:
      return 0
    else:
       T=subset_sum(arr,n,sum(arr))
       for i in range(sum(arr)//2+1):
          if T[n][i]:
             if maxm<i:
                maxm=i
       print(maxm)
       return sum(arr)-2*maxm


if __name__=="__main__":
   print(find_minm_subset_sum_diff([1,5,11,6],4))
          
        
    
    