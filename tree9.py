class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def reverse_level_order(self):
       stack=[]
       queue=[]
       queue.append(self)
       while queue:
           m=queue.pop(0)
           stack.append(m)
           if m.left:
              queue.append(m.left)
           if m.right:
              queue.append(m.right)
       while stack:
          print(stack.pop().value)
  

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
   node.insert(4)
   node.insert(6)
   node.insert(3)
   node.insert(22)
   node.insert(25)
   node.insert(27)
   node.insert(15)
   node.insert(20)
   print("The reverse level order traversal is:")
   node.reverse_level_order()
