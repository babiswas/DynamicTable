def rod_cutting(arr,brr,n,W):
   T=[[-1 for i in range(W+1)] for j in range(n+1)]
   for i in range(n+1):
     for j in range(W+1):
         if i==0 or j==0:
           T[i][j]=0
   for i in range(1,n+1):
      for j in range(1,W+1):
         if i-1>=0:
            if arr[i-1]<=j:
               T[i][j]=max(T[i-1][j],brr[i-1]+T[i][j-arr[i-1]])
            elif arr[i-1]>j:
               T[i][j]=T[i-1][j]
   return T[n][W]


if __name__=="__main__":
   print(rod_cutting([1,2,3,4,5,6,7,8],[1,5,8,9,10,17,17,20],8,8))

   