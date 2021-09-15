def count_subset(arr,n,W):
    if n==0 and W!=0:
       return 0
    elif W==0:
       return 1
    else:
       if n-1>=0:
          if arr[n-1]<=W:
             return count_subset(arr,n-1,W-arr[n-1])+count_subset(arr,n-1,W)
          elif arr[n-1]>W:
             return count_subset(arr,n-1,W)

if __name__=="__main__":
   print(count_subset([1,2,3,3],4,6))
   