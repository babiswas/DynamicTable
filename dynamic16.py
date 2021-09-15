import sys
def minm_coin(arr,n,W):
    if n==0 and W!=0:
       return sys.maxsize
    elif W==0:
       return 0
    else:
       if n-1>=0:
          if arr[n-1]<=W:
             return min(minm_coin(arr,n-1,W),1+minm_coin(arr,n,W-arr[n-1]))
          else:
             return minm_coin(arr,n-1,W)

if __name__=="__main__":
   print(minm_coin([1,2,3],3,5))