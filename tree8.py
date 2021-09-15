class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def level_traversal(self):
       queue=[]
       root=self
       queue.append(root)
       while queue:
          q_len=len(queue)
          if q_len!=0:
             print([obj.value for obj in queue])
          while q_len!=0:
             m=queue.pop(0)
             if m.left:
                queue.append(m.left)
             if m.right:
                queue.append(m.right)
             q_len=q_len-1

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
   node.insert(3)
   node.insert(4)
   node.insert(2)
   node.insert(22)
   node.insert(27)
   node.insert(14)
   node.insert(19)
   node.insert(13)
   print("The level order traversal of the tree is:")
   node.level_traversal()