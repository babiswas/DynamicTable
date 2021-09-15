import sys
class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=None


    def get_index(self,index,visited):
        minm=(sys.maxsize)
        set_index=0
        for i in range(self.vertex):
            if index[i]<minm and visited[i]==False:
                set_index=i
                minm=index[i]
        return set_index


    def display(self,parent):
        for i in range(self.vertex):
            print(f"{parent[i]}-->{i}------{self.graph[parent[i]][i]}")
    
    def prims_algo(self,src):
        index=[sys.maxsize]*self.vertex
        index[src]=0
        visited=[False]*self.vertex
        parent=[-1 for i in range(self.vertex)]
        for i in range(self.vertex):
            element_index=self.get_index(index,visited)
            visited[element_index]=True
            for j in range(self.vertex):
                if self.graph[element_index][j]>0 and self.graph[element_index][j]<index[j] and visited[j]==False:
                    index[j]=self.graph[element_index][j]
                    parent[j]=element_index

        graph.display(parent)


if __name__=="__main__":
    graph=Graph(5)
    graph.graph=[[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
    graph.prims_algo(0)

