import sys
class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


   def postorder(self):
       node=Node(sys.maxsize)
       node.left=self
       root=node
       while root:
           if root.left==None:
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
                 first=root
                 middle=root.left
                 while middle!=root:
                    last=middle.right
                    middle.right=first
                    first=middle
                    middle=last
                 first=root
                 middle=temp
                 while middle!=root:
                    print(middle.value)
                    last=middle.right
                    middle.right=first
                    first=middle
                    middle=last
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
   node.insert(10)
   node.insert(7)
   node.insert(4)
   node.insert(3)
   node.insert(22)
   node.insert(19)
   node.insert(16)
   node.insert(20)
   node.insert(25)
   print("The post order traversal of the tree")
   node.postorder()