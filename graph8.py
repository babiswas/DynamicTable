from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=defaultdict(list)
    
    def add_edges(self,u,v):
        self.graph[u].append(v)
    
    def topsort(self):
        count=0
        indegree=[0]*self.vertex
        for i in range(self.vertex):
            for j in self.graph[i]:
                indegree[j]=indegree[j]+1
        queue=[]
        for i in range(self.vertex):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            m=queue.pop(0)
            print(m)
            for j in self.graph[m]:
                indegree[j]=indegree[j]-1
                if indegree[j]==0:
                    queue.append(j)
            count=count+1
        if count==self.vertex:
            print("Topsort is possible")
        else:
            print("There is a cycle in the graph")


if __name__=="__main__":
    graph=Graph(6)
    graph.add_edges(5,0)
    graph.add_edges(4,0)
    graph.add_edges(5,2)
    graph.add_edges(2,3)
    graph.add_edges(3,1)
    graph.add_edges(4,1)
    graph.topsort()
    print("Creating another graph")
    graph1=Graph(4)
    graph1.add_edges(0,2)
    graph1.add_edges(2,0)
    graph1.add_edges(2,3)
    graph1.add_edges(3,3)
    graph1.add_edges(0,1)
    graph1.add_edges(1,2)
    graph1.topsort()
    