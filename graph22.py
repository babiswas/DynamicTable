class Cell:
   def __init__(self,x,dist):
         self.x=x
         self.dist=dist
         

def min_hops(x,y):
      queue=[]
      queue.append(Cell(x,0))
      s=set()
      s.add(x)
      while queue:
            m=queue.pop(0)
            if m.x==y:
               return m.dist
            else:
                  x1=m.x*2
                  x2=m.x-1
                  if x1 not in s:
                     queue.append(Cell(x1,m.dist+1))
                     s.add(x1)
                  if x2 not in s:
                     queue.append(Cell(x2,m.dist+1))
                     s.add(x2)


if __name__=="__main__":
   print(min_hops(4,7))
           
              
    
    