class newNode:
  def __init__(self,data): 
    self.data = data 
    self.left = self.right = None
def mirror(node): 
  if (node == None): 
    return
  else:
    temp = node 
    mirror(node.left) 
    mirror(node.right)
    temp = node.left 
    node.left = node.right 
    node.right = temp 
def inOrder(node) : 
  if (node == None): 
    return
    inOrder(node.left) 
    print(node.data, end = " ") 
    inOrder(node.right) 
if __name__ =="__main__": 
  '''root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) '''
  rb=list(map(int,input().split()))
  for i in range (len(rb)):
    root=newNode(input())
    inOrder(root) 

