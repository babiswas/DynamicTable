class Cell:
    def __init__(self,x,y,dist):
        self.x=x
        self.y=y
        self.dist=dist


def isvalid(x,y,L):
    if x<0 or x>=L:
        return False
    if y<0 or y>=L:
        return False
    return True



def  min_hops(start,target,M):
    dx=[2,2,-2,-2,1,-1,1,-1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    visited=[[False for i in range(M)] for i in range(M)]
    queue=[]
    queue.append(Cell(start[0],start[1],0))
    visited[start[0]][start[1]]=True
    while queue:
        m=queue.pop(0)
        if m.x==target[0] and m.y==target[1]:
            return m.dist
        else:
            for i in range(8):
                x=m.x+dx[i]
                y=m.y+dy[i]
                if isvalid(x,y,M) and visited[x][y]==False:
                    queue.append(Cell(x,y,m.dist+1))
                    visited[x][y]=True



if __name__=="__main__":
    start=(1,1)
    target=(4,3)
    print(min_hops(start,target,5))

