def rod_cutting(arr,brr,n,W):
    if n==0 or W==0:
       return 0
    else:
       if n-1>=0:
          if arr[n-1]<=W:
             return max(rod_cutting(arr,brr,n-1,W),brr[n-1]+rod_cutting(arr,brr,n,W-arr[n-1]))
          else:
             return rod_cutting(arr,brr,n-1,W)


if __name__=="__main__":
   print(rod_cutting([1,2,3,4,5,6,7,8],[1,5,8,9,10,17,17,20],8,8))
   