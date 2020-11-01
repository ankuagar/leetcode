class InorderIterator(object):
  """
  This constructor implementation uses O(N) memory to keep all nodes in memory in inorder in deque called self.inorder,
  once the consutruction is over

  During construction, at any time all visited nodes are in memory, either in self.inorder or stack
  By using extra memory, getNext is able to be implemented in O(1) time
  Time is O(N) since all nodes need to be visited
  This implementation does not modify the original tree
  """
  def __init__(self, root):
    from collections import deque
    if root is None: # tree is empty
        raise Exception("Iteration not possible on empty tree")
    self.inorder = deque() # contains nodes in "inorder" insert from left and pop from right (inorder starts from right end)
    stack = [] # order in which nodes are processed
    while len(stack) > 0 or root is not None:
      if root is not None:
          stack.append(root)
          root = root.left
          continue
      temp = stack.pop()
      self.inorder.appendleft(temp) # append at left end
      root = temp.right

  def hasNext(self):
    return len(self.inorder) > 0

  def getNext(self):
    '''
    Will throw an exception if called despite hasNext returning False
    '''
    return self.inorder.pop().data # pop from right end

class InorderIterator1(object):
  """
  This implementation uses O(h) memory at any time (h = height of the tree) to store nodes in stack inorder
  Since not all nodes are in memory, getNext has to spend time every so often to replenish the stack that stores the
  nodes inorder
  Time is O(N) since all nodes need to be visited
  This implementation does not modify the original tree
  """
  def __populate_inorder_stack(self, root):
      self.inorder.append(root)
      while root.left is not None:
          root = root.left
          self.inorder.append(root)

  def __init__(self, root):
    if root is None: # tree is empty
        raise Exception("Iteration not possible on empty tree")
    self.inorder = [] # pop from right to get nodes in inorder
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
    return temp.data

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        def insert_helper(root, val):        
            if root is None:
                return TreeNode(val)
            elif val < root.data:
                root.left =  insert_helper(root.left, val)
            elif val > root.data:
                root.right = insert_helper(root.right, val)
            return root 
        self.root = insert_helper(self.root, val)
    
    def pre_order(self):
        preorder = []
        def pre_order_helper(root):
            if root is None:
                return
            else:
                preorder.append(root.data)
                pre_order_helper(root.left)
                pre_order_helper(root.right)
        pre_order_helper(self.root)
        return preorder

    def inorder_iterative(self):
        '''
        Since it stores the nodes inorder in list inorder the memory usage is O(N)
        If it was simply printing the node data inoder then the memory usage will be O(h), h = height of tree
        Time is O(N) since all nodes need to be visited
        This implementation does not modify the original tree
        '''
        inorder = []
        # if self.root is None:
        #     stack = []
        # else:
        #     stack = [self.root]
        stack = []
        root = self.root
        while len(stack) > 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
                continue
            temp = stack.pop()
            inorder.append(temp.data)
            root = temp.right
        return inorder

    def inorder_successor(self, d):
        '''
        In inorder traversal the successor of a given value is always larger than the given value
        It is the smallest number which is larger than the given value d
        Memory usage is O(1) since it only stores the successor at any given point
        Runtime is O(h), h = height of tree since it visits the leaf node at maximum depth in the worst case
        '''
        successor = None
        root = self.root
        while root is not None:
            if d < root.data: # value less than current Node
                successor = root # make current Node as successor
                root = root.left # go left
            elif d > root.data: # if value greator than current Node
                root = root.right # go right
            else:
                if root.right is None:
                        return successor.data if successor is not None else None
                else:
                    # return the smallest number which is larger than the given value d
                    successor = root.right 
                    while successor.left is not None:
                        successor = successor.left
                    return successor.data
        return None # if value d is not found, return None

    @staticmethod
    def are_identical(root1, root2):
        if root1 == root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        elif root1.data != root2.data:
            return False
        elif root1.data == root2.data:
            return Tree.are_identical(root1.left, root2.left) and Tree.are_identical(root1.right, root2.right)


    



