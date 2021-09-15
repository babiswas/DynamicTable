def subset_sum(arr,n,W):
   if n==0 and W!=0:
      return False
   elif W==0:
      return True
   else:
      if n-1>=0:
         if arr[n-1]<=W:
            return subset_sum(arr,n-1,W-arr[n-1]) or subset_sum(arr,n-1,W)
         elif arr[n-1]>W:
            return subset_sum(arr,n-1,W)

def equal_sum_partition(arr,n,W):
    sum=0
    for i in arr:
      sum=sum+i
    if sum%2==0:
       return subset_sum(arr,n,sum//2)
    else:
       return False

if __name__=="__main__":
   print(equal_sum_partition([1,5,11,5],4,11))
  