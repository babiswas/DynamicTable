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

   def mirror(self):
       if self:
          temp=self.left
          self.left=self.right
          self.right=temp
          if self.left:
             self.left.mirror()
          if self.right:
             self.right.mirror()
       

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
   node.insert(9)
   node.insert(10)
   node.insert(7)
   node.insert(4)
   node.insert(3)
   node.insert(22)
   node.insert(25)
   node.insert(19)
   node.insert(20)
   node.insert(16)
   print("The inorder tarversal of the tree is")
   node.inorder()
   print("Mirroring the tree")
   node.mirror()
   print("The inorder traversal of the tree after mirroring the tree is:")
   node.inorder()