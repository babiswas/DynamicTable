class Cell:
    def __init__(self,parent,rank):
        self.parent=parent
        self.rank=rank

    def __str__(self):
        return f"{self.parent} and {self.rank}"


class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=[]

    def add_edges(self,u,v,w):
        self.graph.append((u,v,w))


    def find(self,u,rank):
        while rank[u].parent!=u:
            u=rank[u].parent
        return u


    def union(self,index1,index2,rank):
        if rank[index1].parent>rank[index2].parent:
            rank[index2].parent=index1
            rank[index1].rank+=1
        else:
            rank[index1].parent=index2
            rank[index2].rank+=1


    def kruskal_algo(self):
        edge_list=[]
        rank=[Cell(i,0) for i in range(self.vertex)]
        def getitem(obj):
            return obj[2]
        self.graph=sorted(self.graph,key=getitem)
        for u,v,w in self.graph:
            print([str(obj) for obj in rank])
            index1=self.find(u,rank)
            index2=self.find(v,rank)
            if index1!=index2:
               edge_list.append((u,v,w))
               self.union(index1,index2,rank)
        print(edge_list)


if __name__=="__main__":
    graph=Graph(9)
    graph.add_edges(0,1,4)
    graph.add_edges(0,7,8)
    graph.add_edges(1,7,11)
    graph.add_edges(1,2,8)
    graph.add_edges(7,6,1)
    graph.add_edges(7,8,7)
    graph.add_edges(8,6,6)
    graph.add_edges(2,8,2)
    graph.add_edges(6,5,2)
    graph.add_edges(2,5,4)
    graph.add_edges(2,3,7)
    graph.add_edges(3,5,14)
    graph.add_edges(5,4,10)
    graph.add_edges(3,4,9)
    print("Displaying minimum spanning tree using krushkal algo")
    graph.kruskal_algo()



