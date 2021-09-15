def unbounded_knapsack(arr,brr,n,W):
    if n==0 or W==0:
       return 0
    else:
       if n-1>=0:
          if arr[n-1]<=W:
             return max(unbounded_knapsack(arr,brr,n-1,W),brr[n-1]+unbounded_knapsack(arr,brr,n,W-arr[n-1]))
          elif arr[n-1]>W:
             return unbounded_knapsack(arr,brr,n-1,W)


if __name__=="__main__":
   print(unbounded_knapsack([1,3,4,5],[10,40,50,70],4,8))