class Node:
    def __init__(self,data, left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    def insert (self,val):
        if self.root == None:
            self.root =  Node(val)
        else :
            self._insert(val,self.root)
    def _insert(self,val,node):
        if val < node.data:
            if node.left == None:
                node.left = Node(val)
                return
            self._insert(val,node.left)
        elif val > node.data:
            if node.right == None:
                node.right = Node(val)
                return
            self._insert(val,node.right)
    def inorder(self):
        if self.root == None :
            print("Tree is Empty")
        else:
            self._inorder(self.root)
    def _inorder(self,root):
        if root.left != None:
            self._inorder(root.left)
        print(root.data)
        if root.right != None:
            self._inorder(root.right)
    def search(self,val):
        return self._search(val,self.root)
    def _search(self, val ,root):
        if root == None:
            return False
        else:
            if val == root.data:
                return True
            elif val < root.data:
                return self._search(val,root.left)
            elif val > root.data:
                return self._search(val,root.right)
        return -1
    def delet(self,val):
        self._delet(val,self.root)
    def _delet(self,val,root):
        if root == None:
            return None
        if val < root.data:
            root.left = self._delet(val,root.left)
        elif val > root.data:
            root.right = self._delet(val,self.right)
        else:
            if root.left == None:
                return root.right
            elif root.right ==None:
                return root.left
            else:
                temp = self.successer(root.right)
                #print(root.data)
                # print(temp.data)
                root.data = temp.data
                root.right = self._delet(temp.data,root.right)
        return root
    def successer(self,root):
        current =  root 
        while current.left != None:
            current = current.left
        return current
bst = Binary_Search_Tree()
arr = [8,5,12,17,10,13,1,3,4,6,8]
for i in arr:
    bst.insert(i)
bst.inorder()
bst.delet(5)
# print("damal")
bst.inorder()
# print(bst.search(10))