class node:
    
    def __init__(self,val,parent=None):
        self.name = val
        self.children=[]
        self.parent = parent
    
    def __repr__(self):
        return self.name

'''class Tree:
    
    def __init__(self,root):
        self.root = root'''

def search(root,val):
    queue = [root]
    while len(queue)>0:
        temp = queue.pop(0)
        if(temp.name==val):
            return temp
        queue.extend(temp.children)
    return None
        
def display(root):
    queue = [root]
    t = root.parent
    while len(queue)>0:
        temp = queue.pop(0)
        if temp.parent != t:
            t = temp.parent
            print()
        print(temp.name,end = " ")
        queue.extend(temp.children)
        
def subrole(child,parent):
    
    pnode = search(root,parent)
    pnode.children.append(node(child,pnode))

def delete(node1,node2):
    node1 = search(root,node1)
    node2 = search(root,node2)
    node2.children.extend(node1.children)
    node1.parent.children.remove(node1)
    for node in node1.children:
        node.parent = node2
    
    

root = node(input('Enter name of root node: '))
#child,parent = input('Enter subrole and role: ').split(' ')
subrole('CTO','CEO')
subrole('COO','CEO')
subrole('CPO','CTO')
subrole('ABC','CTO')
delete('CTO','CEO')
#print(root.children)
display(root)