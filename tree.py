class TreeNode:
    def __init__(self,key,left = None, right= None, parent = None):
        self.value = key
        self.left_child = left
        self.right_child = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.left_child

    def hasrightChild(self):
        return self.right_child
    
    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        return self.parent and self.parent.right_child == self
    
    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.hasLeftChild() or self.hasrightChild())

    

class ArbolBinario:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    def _put(self, key, currentNode):
        if key < currentNode.value:
            if currentNode.hasLeftChild():
                self._put(key,currentNode.left_child)
            else:
                currentNode.left_child = TreeNode(key,parent=currentNode)
        else:
            if currentNode.hasrightChild():
                self._put(key,currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key,parent=currentNode)

    def showtree(self,currentNode):
        print(currentNode.value)
        if currentNode.hasLeftChild():
            self.showtree(currentNode.left_child)
        if currentNode.hasrightChild():
            self.showtree(currentNode.right_child)



arbol = ArbolBinario()

arbol.put(1)
arbol.put(2)
arbol.put(0)

arbol.showtree(arbol.root)