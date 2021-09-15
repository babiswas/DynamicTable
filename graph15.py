class Cell:
    def __init__(self,x,y,dist):
        self.x=x
        self.y=y
        self.dist=dist


def is_valid(x,y,M,N):
    if x<0 or x>=N:
        return False
    if y<0 or y>=N:
        return False
    if M[x][y]=='#':
        return False
    return True



def min_hops(start,target,M,N):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited=[[False for i in range(N)] for i in range(N)]
    queue=[]
    queue.append(Cell(start[0],start[1],0))
    visited[start[0]][start[1]]=True
    while queue:
        m=queue.pop(0)
        if m.x==target[0] and m.y==target[1]:
            return m.dist
        else:
            for i in range(4):
                x=m.x+dx[i]
                y=m.y+dy[i]
                if is_valid(x,y,M,N) and visited[x][y]==False:
                    queue.append(Cell(x,y,m.dist+1))
                    visited[x][y]=True

if __name__=="__main__":
    M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
    start=[0,2]
    target=[2,0]
    print(min_hops(start,target,M,4))
