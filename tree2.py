class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       stack=[]
       root=self
       while True:
          if root:
             stack.append(root)
             root=root.left
          elif stack:
             root=stack.pop()
             print(root.value)
             root=root.right
          else:
             break

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
   node.insert(3)
   node.insert(7)
   node.insert(4)
   node.insert(21)
   node.insert(14)
   node.insert(25)
   node.insert(23)
   print("The inorder traversal of the tree is")
   node.inorder()