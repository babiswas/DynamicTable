from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def BFS(self,u,level):
       count=0
       visited=[False]*self.vertex
       queue=[]
       queue.append(u)
       visited[u]=True
       while queue:
          num=len(queue)
          if num!=0:
             count=count+1
          if count==level:
             print(queue)
             return
          while num:
              sample=queue.pop(0)
              for u in self.graph[sample]:
                 if not visited[u]:
                    queue.append(u)
                    visited[u]=True
              num=num-1

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.BFS(2,1)
   graph.BFS(2,2)
   graph.BFS(2,3)
       