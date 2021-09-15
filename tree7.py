class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       stack1=[]
       stack2=[]
       root=self
       stack1.append(root)
       while stack1:
           ptr=stack1.pop()
           stack2.append(ptr)
           if ptr.left:
              stack1.append(ptr.left)
           if ptr.right:
              stack1.append(ptr.right)
       print(stack2)
       while stack2:
         print(stack2.pop().value)
           

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
   node.insert(7)
   node.insert(5)
   node.insert(9)
   node.insert(4)
   node.insert(6)
   node.insert(22)
   node.insert(25)
   node.insert(20)
   node.insert(14)
   print("The post order traversal of the tree is")
   node.postorder()
   