class InorderIterator(object):
  """
  This constructor implementation uses O(N) memory to keep all nodes in memory in inorder in deque called self.inorder, once the consutruction is over

  During construction, at any time all visited nodes are in memory, either in self.inorder or stack
  By using extra memory, getNext is able to be implemented in O(1) time
  Time is O(N) since all nodes need to be visited
  """
  def __init__(self, root):
    from collections import deque
    if root is None: # tree is empty
        raise Exception("Iteration not possible on empty tree")
    self.inorder = deque() # contains nodes in "inorder" insert from left and pop from right (inorder starts from rightmost end)
    stack = [] # order in which nodes are processed
    stack.append(root)
    while len(stack) > 0:
      current = stack[-1]
      if current.left is not None:
        stack.append(current.left)
      else:
        stack.pop()
        if len(stack) > 0:
          stack[-1].left = None
        self.inorder.appendleft(current)
        if current.right is not None:
          stack.append(current.right)

  def hasNext(self):
    return len(self.inorder) > 0

  def getNext(self):
    '''
    Will throw an exception if called despite hasNext returning False
    '''
    return self.inorder.pop().val

class InorderIterator1(object):
  """
  This implementation uses O(h) memory at any time to store nodes equal to the height of the tree where
  h = height of the tree
  Since not all nodes are in memory, getNext has to spend time every so often to replenish the stack that stores the
  nodes inorder
  Time is O(N) since all nodes need to be visited
  """
  def __populate_inorder_stack(self, root):
      self.inorder.append(root)
      while root.left is not None:
          root = root.left
          self.inorder.append(root)

  def __init__(self, root):
    if root is None: # tree is empty
        raise Exception("Iteration not possible on empty tree")
    self.inorder = [] # contains nodes in "inorder" insert from left and pop from right (inorder starts from rightmost end)
    self.__populate_inorder_stack(root)

  def hasNext(self):
    return len(self.inorder) > 0

  def getNext(self):
    '''
    Will throw an exception if called despite hasNext returning False
    '''
    temp = self.inorder.pop()
    if temp.right is not None: # populate self.inorder with the right subtree of the given node
        self.__populate_inorder_stack(temp.right)
    return temp.val

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

    def inorder_iterative(self):
        '''
        Since it stores the nodes inorder in list inorder the memory usage is O(N)
        If it was simply printing the node data inoder then the memory usage will be O(h), h = height of tree
        Time is O(N) since all nodes need to be visited
        '''
        inorder = []
        if self.root is None:
            stack = []
        else:
            stack = [self.root]
        while len(stack) > 0:
            temp = stack[-1]
            if temp.left is not None:
                stack.append(temp.left)
            else:
                stack.pop()
                if len(stack) > 0:
                    stack[-1].left = None
                if temp.right is not None:
                    stack.append(temp.right)
                inorder.append(temp.val)
        return inorder

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


    



