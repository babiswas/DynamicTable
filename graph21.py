class Cell:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist

def isvalid(x,N):
    if x<0 or x>=N:
       return False
    return True

def min_hops(start,N,arr):
    dx=[1,-1]
    visited=[False]*N
    queue=[]
    queue.append(Cell(0,0))
    visited[0]=True
    while queue:
       m=queue.pop(0)
       if m.x==N-1:
         return m.dist
       else:
          for i in range(2):
             x=m.x+dx[i]
             if isvalid(x,N) and visited[x]==False:
                queue.append(Cell(x,m.dist+1))
                visited[x]=True
          indexes=[i for i,j in enumerate(arr) if j==arr[m.x]]
          for i in indexes:
            if isvalid(i,N) and visited[i]==False:
               queue.append(Cell(i,m.dist+1))
               visited[i]=True
if __name__=="__main__":
   l=[0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
   print(min_hops(0,len(l),l))
          
    