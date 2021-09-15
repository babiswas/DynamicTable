def BFS(m,n,stepping_num):
      queue=[]
      queue.append(stepping_num)
      while queue:
            num=queue.pop(0)
            if num>=m and num<=n:
                  print(num)
            elif num<m or num>n:
                  continue
            last_digit=num%10
            num1=num*10+(last_digit-1)
            num2=num*10+(last_digit+1)
            if last_digit==0:
               queue.append(num2)
            elif last_digit==9:
               queue.append(num1)
            else:
               queue.append(num1)
               queue.append(num2)


def stepping_num(m,n):
    for i in range(10):
       BFS(m,n,i)
    

if __name__=="__main__":
   stepping_num(0,21)
           