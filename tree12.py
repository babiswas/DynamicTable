from collections import defaultdict
class Node:

   def topview(self):
       global_map=defaultdict(list)
       queue=[]
       queue.append((self,0))
       while queue:
           m=queue.pop(0)
           global_map[m[1]].append(m[0])
           if m[0].left:
              queue.append((m[0].left,m[1]-1))
           if m[0].right:
              queue.append((m[0].right,m[1]+1))
       print("The top view of the tree is")
       for key in sorted(global_map.keys()):
           print(global_map[key][0].value)
       print("the bottom view of the tree is:")
       for key in sorted(global_map.keys()):
           print(global_map[key][-1].value)
           
           
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

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
   print("The top and bottom view of the tree is:")
   node.topview()