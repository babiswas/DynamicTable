def stepping_number(m,n):
      temp1=0
      temp2=0
      stepping_num=[]
      for i in range(m,n):
         if is_stepping_num(i):
            stepping_num.append(i)
      return stepping_num


def is_stepping_num(num):
    queue=[]
    num1=num
    while num1:
       unitplace=num1%10
       num1=num1//10
       queue.append(unitplace)
    while queue:
        m=queue.pop(0)
        if not queue:
           return True
        else:
           if abs(queue[0]-m)!=1:
              return False

if __name__=="__main__":
   print(stepping_number(10,16))
   print(stepping_number(0,22))
   