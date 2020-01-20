
TODO: 
1. Try iterative solutions for preorder, inorder, postorder traversals
2. Improve level order traversal with DFS & BFS concepts

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root): # Recursive
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        if root is None:
            return preorder
        preorder.append(root.val)
        preorder += self.preorderTraversal(root.left)
        preorder += self.preorderTraversal(root.right)
        return preorder



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        if root is None:
            return inorder
        
        inorder += self.inorderTraversal(root.left)
        inorder.append(root.val)
        inorder += self.inorderTraversal(root.right)
        return inorder 
                
                
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder = []
        if root is None:
            return postorder
        postorder += self.postorderTraversal(root.left)
        postorder += self.postorderTraversal(root.right)
        postorder.append(root.val)
        return postorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_order = []
        q = deque()
        if root is None:
            return level_order
        q.append([root])
        while len(q) != 0:
            current_level_values = [] # for level_order
            next_level = [] # for q
            current_level_nodes = q.popleft()
            for node in current_level_nodes:
                current_level_values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if len(current_level_values) > 0:
                level_order.append(current_level_values)
            
            if len(next_level) > 0:
                q.append(next_level)
        return level_order
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth1(self, root): 
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Uses bottoms-up approach
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
    def maxDepth(self, root): 
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Uses top down approach
        """
        def helper(root, parent_depth):
            if root is None:
                return parent_depth
            current_depth = 1 + parent_depth
            left_depth = helper(root.left, current_depth)
            right_depth = helper(root.right, current_depth)
            return max(left_depth, right_depth)
            
        return helper(root,0)                        
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Solution(object):
    def isPalindrome(self, l):
        """
        :type l: List[TreeNode]
        :rtype: bool
        """
        def mapper(obj):
            if obj is None:
                return None
            else:
                return obj.val
        l = map(mapper, l)    
        length = len(l)
        for i in xrange(length/2):
            if l[i] != l[length-1-i]:
                return False
        return True            
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        q = deque()
        q.append([root])
        while len(q) != 0:
            next_level_nodes = []
            current_level_nodes = q.popleft()
            for node in current_level_nodes:
                if node is not None:
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
            if len(next_level_nodes) == 0:
                return True
            elif self.isPalindrome(next_level_nodes):
                q.append(next_level_nodes)  
            else:
                return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        top down approach
        """
        def helper(root, cs, sum):
            if root is None:
                return False 
            cs = cs + root.val
        
            if root.left is None and root.right is None:
                return cs == sum
            else:
                return helper(root.left, cs, sum) or helper(root.right,cs, sum)

        if root is None:
            return False
        
        return helper(root, 0, sum)        
