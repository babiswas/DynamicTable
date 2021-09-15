def subset_sum(arr,n,W):
   if n==0 and W!=0:
      return False
   elif W==0:
      return True
   else:
      if n-1>=0:
         if arr[n-1]>W:
            return subset_sum(arr,n-1,W)
         elif arr[n-1]<=W:
            return subset_sum(arr,n-1,W) or subset_sum(arr,n-1,W-arr[n-1])

if __name__=="__main__":
   print(subset_sum([3, 34, 4, 12, 5, 2],6,9))
