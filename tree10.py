class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


   def inorder(self):
      if self:
         if self.left:
            self.left.inorder()
         print(self.value)
         if self.right:
            self.right.inorder()
   
   def level_order_trav(self):
       queue=[]
       stack=[]
       queue.append(self)
       while queue:
           m=queue.pop(0)
           stack.append(m)
           if m.right:
              queue.append(m.right)
           if m.left:
              queue.append(m.left)
       while stack:
           m=stack.pop()
           print(m.value)
           
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
    node.insert(22)
    node.insert(7)
    node.insert(9)
    node.insert(6)
    node.insert(25)
    node.insert(27)
    node.insert(14)
    print("The inorder traversal of the tree is")
    node.inorder()
    print("The level order traversal of the graph is")
    node.level_order_trav()