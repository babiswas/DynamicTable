def knapsack_dp(arr,brr,n,W):
    T=[[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
      for j in range(W+1):
         if i==0 or j==0:
            T[i][j]=0
    for i in range(1,n+1):
       for j in range(1,W+1):
             if i-1>=0:
                if arr[i-1]<=j:
                   T[i][j]=max(brr[i-1]+T[i-1][j-arr[i-1]],T[i-1][j])
                elif arr[i-1]>j:
                   T[i][j]=T[i-1][j]
    return T[n][W]

if __name__=="__main__":
   arr=[1,3,4,5]
   brr=[1,4,5,7]
   print(knapsack_dp(arr,brr,4,7))
   
    