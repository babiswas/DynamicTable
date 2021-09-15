class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=[]

    def add_edges(self,u,v):
        self.graph.append((u,v))

    def find(self,u,arr):
        while arr[u]!=-1:
            u=arr[u]
        return u


    def union(self,parent,u,v):
        index1=self.find(u,parent)
        index2=self.find(v,parent)
        if index1!=index2:
            parent[u]=v

    def is_cycle(self):
        arr=[-1 for i in range(self.vertex)]
        for u,v in self.graph:
           print(arr)
           index1=self.find(u,arr)
           index2=self.find(v,arr)
           print(f"{index1}  and {index2}")
           if index1==index2:
              return True
           else:
              self.union(arr,index1,index2)
        return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(4,1)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   print(graph.is_cycle())
   print("Creating another graph")
   graph=Graph(6)
   graph.add_edges(4,1)
   graph.add_edges(4,0)
   graph.add_edges(5,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   print(graph.is_cycle())