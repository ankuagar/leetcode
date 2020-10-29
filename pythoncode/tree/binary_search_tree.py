#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        def insert_helper(root, val):        
            if root is None:
                return TreeNode(val)
            elif val < root.val:
                root.left =  insert_helper(root.left, val)
            elif val > root.val:
                root.right = insert_helper(root.right, val)
            return root 
        self.root = insert_helper(self.root, val)
    
    def pre_order(self):
        preorder = []
        def pre_order_helper(root):
            if root is None:
                return
            else:
                preorder.append(root.val)
                pre_order_helper(root.left)
                pre_order_helper(root.right)
        pre_order_helper(self.root)
        return preorder

    @staticmethod
    def are_identical(root1, root2):
        if root1 == root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        elif root1.val != root2.val:
            return False
        elif root1.val == root2.val:
            return Tree.are_identical(root1.left, root2.left) and Tree.are_identical(root1.right, root2.right)


    



