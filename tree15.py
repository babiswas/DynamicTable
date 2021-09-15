class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def recursive_preorder(self):
       if self:
          print(self.value)
          if self.left:
             self.left.recursive_preorder()
          if self.right:
             self.right.recursive_preorder()


   def inorder(self):
       root=self
       while root:
          root=self
          while root:
             if root.left==None:
                print(root.value)
                root=root.right
             else:
                temp=None
                temp=root.left
                while temp.right!=root and temp.right!=None:
                    temp=temp.right
                if temp.right!=root:
                   temp.right=root
                   root=root.left
                elif temp.right==root:
                   print(root.value)
                   temp.right=None
                   root=root.right
          

   def preorder(self):
       root=self
       while root:
          if root.left==None:
             print(root.value)
             root=root.right
          else:
             temp=None
             temp=root.left
             while temp.right!=None and temp.right!=root:
                   temp=temp.right
             if temp.right!=root:
                temp.right=root
                print(root.value)
                root=root.left
             elif temp.right==root:
                temp.right=None
                root=root.right

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
   node.insert(4)
   node.insert(10)
   node.insert(7)
   node.insert(22)
   node.insert(19)
   node.insert(16)
   node.insert(20)
   node.insert(25)
   print("The preorder tarversal of the tree is:")
   node.recursive_preorder()
   print("Iterative")
   node.preorder()
   print("The inorder traversal of the tree is:")
   node.inorder()
