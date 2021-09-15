def subset_sum(arr,n,W):
    if n==0 and W!=0:
       return False
    elif W==0:
       return True
    else:
        if n-1>=0:
           if arr[n-1]<=W:
              return subset_sum(arr,n-1,W) or subset_sum(arr,n-1,W-arr[n-1])
           else:
              return subset_sum(arr,n-1,W)
       

def minm_difference(arr,n):
    s_list=[False for i in range(sum(arr)//2+1)]
    for i in range(sum(arr)//2+1):
        if subset_sum(arr,n,i):
          s_list[i]=True
    print(s_list)
    return sum(arr)-2*max([x for x,y in enumerate(s_list) if y==True])



if __name__=="__main__":
   print(minm_difference([1,6,11,5],4))
   
           
       
           
    
    

    
    
    