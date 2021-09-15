def knapsack(arr,brr,n,W):
    if n==0 or W==0:
       return 0
    elif arr[n-1]>W:
       return knapsack(arr,brr,n-1,W)
    elif arr[n-1]<=W:
       return max(knapsack(arr,brr,n-1,W),knapsack(arr,brr,n-1,W-arr[n-1])+brr[n-1])

def knapsack_dp(arr,brr,W,n,dp):
    if n==0 or W==0:
      dp[n][W]=0
      return dp[n][W]
    if n-1>=0:
       if dp[n][W]!=-1:
          return dp[n][W]
       else:
          if arr[n-1]>W:
             dp[n][W]=knapsack_dp(arr,brr,W,n-1,dp)
          if arr[n-1]<=W:
             dp[n][W]=max(knapsack_dp(arr,brr,W,n-1,dp),knapsack_dp(arr,brr,W-arr[n-1],n-1,dp)+brr[n-1])
          return dp[n][W]

def knapsack_DP(arr,brr,n,W):
    dp=[[-1 for i in range(W+1)] for j in range(n+1)]
    return knapsack_dp(arr,brr,W,n,dp)
    

if __name__=="__main__":
   print(knapsack([1,3,4,5],[1,4,5,7],4,7))
   print("Dp after memoization")
   print(knapsack_DP([1,3,4,5],[1,4,5,7],4,7))
   



