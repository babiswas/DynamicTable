class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def print_root_path(self):
       stack=[]
       root=self
       while True:
          if root:
             stack.append(root)
             root=root.left
          else:
             if not stack:
                break
             if stack[-1].right==None:
                print([obj.value for obj in stack])
                root=stack.pop()
                while stack[-1].right==root:
                    print([obj.value for obj in stack])
                    root=stack.pop()
                    if not stack:
                       break
             if stack:
                 root=stack[-1].right
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
   node.insert(7)
   node.insert(10)
   node.insert(5)
   node.insert(4)
   node.insert(22)
   node.insert(25)
   node.insert(23)
   node.insert(17)
   node.insert(20)
   print("Root to vertex for the graph is:")
   node.print_root_path()