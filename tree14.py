from collections import defaultdict
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

   def vertical_order(self):
       global_list=defaultdict(list)
       queue=[]
       queue.append((self,0))
       while queue:
           m=queue.pop(0)
           global_list[m[1]].append(m[0])
           if m[0].left:
              queue.append((m[0].left,m[1]-1))
           if m[0].right:
              queue.append((m[0].right,m[1]+1))
       return global_list

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
   node.insert(7)
   node.insert(10)
   node.insert(4)
   node.insert(3)
   node.insert(22)
   node.insert(25)
   node.insert(19)
   node.insert(20)
   node.insert(16)
   print("The inorder traversal of the tree is:")
   node.inorder()
   print("The vertical order traversal of the tree is")
   l=node.vertical_order()
   for key in sorted(l.keys()):
     print([obj.value for obj in l[key]])