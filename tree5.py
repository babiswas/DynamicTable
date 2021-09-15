class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def height(self):
       queue=[]
       queue.append(self)
       count=0
       while queue:
          q_len=len(queue)
          if q_len:
             count=count+1
          else:
             return count
          while q_len:
              m=queue.pop(0)
              if m.left:
                 queue.append(m.left)
              if m.right:
                 queue.append(m.right)
              q_len=q_len-1
       return count
   
             
   def insert(self,value):
       if self.value>value:
          if self.left:
             self.left.insert(value)
          else:
             self.left=Node(value)
       elif self.value<value:
          if self.right:
             self.right.insert(value)
          else:
             self.right=Node(value)
       else:
          print("Duplication not allowed")


if __name__=="__main__":
   node=Node(12)
   node.insert(5)
   node.insert(7)
   node.insert(6)
   node.insert(9)
   node.insert(4)
   node.insert(2)
   node.insert(21)
   node.insert(14)
   node.insert(25)
   node.insert(23)
   print("the height of the tree")
   print(node.height())