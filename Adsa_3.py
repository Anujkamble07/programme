# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

# # Function to insert in BST
#     def insert(self, data):
#         # if value is lesser than the value of the parent node
#         if data < self.data:
#             if self.leftChild:
#                 # if we still need to move towards the left subtree
#                 self.leftChild.insert(data)
#             else:
#                 self.leftChild = Node(data)
#                 return
#         # if value is greater than the value of the parent node        
#         else:
#             if self.rightChild:
#                 # if we still need to move towards the right subtree
#                 self.rightChild.insert(data)
#             else:
#                 self.rightChild = Node(data)
#                 return

#     # function to print a BST
#     def PrintTree(self):
#         if self.leftChild:
#             self.leftChild.PrintTree()
#         print( self.data),
#         if self.rightChild:
#             self.rightChild.PrintTree()

# # Creating root node
# root = Node(27)
# # Inserting values in BST
# root.insert(14)
# root.insert(35)
# root.insert(31)
# root.insert(10)
# root.insert(19)
# # printing BST
# root.PrintTree()

##***********height of tree************##

# class Node:
 
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
 
# # Compute the "maxDepth" of a tree -- the number of nodes
# # along the longest path from the root node down to the
# # farthest leaf node
 
 
# def maxDepth(node):
#     if node is None:
#         return 0
 
#     else:
 
#         # Compute the depth of each subtree
#         lDepth = maxDepth(node.left)
#         rDepth = maxDepth(node.right)
 
#         # Use the larger one
#         if (lDepth > rDepth):
#             return lDepth+1
#         else:
#             return rDepth+1
 
 
# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
 
 
# print("Height of tree is %d" % (maxDepth(root)))

####**************inorder,preorder,postorder***********###
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
 
 
# # A function to do inorder tree traversal
# def printInorder(root):
 
#     if root:
 
#         # First recur on left child
#         printInorder(root.left)
 
#         # then print the data of node
#         print(root.val),
 
#         # now recur on right child
#         printInorder(root.right)
 
 
# # Driver code
# if __name__ == "__main__":
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
 
#     # Function call
#     print ("\nInorder traversal of binary tree is")
#     printInorder(root)
# ##*********preorder************##
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
 
 
# # A function to do preorder tree traversal
# def printPreorder(root):
 
#     if root:
 
#         # First print the data of node
#         print(root.val),
 
#         # Then recur on left child
#         printPreorder(root.left)
 
#         # Finally recur on right child
#         printPreorder(root.right)
 
 
# # Driver code
# if __name__ == "__main__":
#   root = Node(1)
#   root.left = Node(2)
#   root.right = Node(3)
#   root.left.left = Node(4)
#   root.left.right = Node(5)
 
#   # Function call
#   print ("Preorder traversal of binary tree is")
#   printPreorder(root)

# ##**********postorder***********##
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
 
# # A function to do postorder tree traversal
# def printPostorder(root):
 
#     if root:
 
#         # First recur on left child
#         printPostorder(root.left)
 
#         # the recur on right child
#         printPostorder(root.right)
 
#         # now print the data of node
#         print(root.val),
 
 
# # Driver code
# if __name__ == "__main__":
#   root = Node(1)
#   root.left = Node(2)
#   root.right = Node(3)
#   root.left.left = Node(4)
#   root.left.right = Node(5)
 
#   # Function call
#   print ("\nPostorder traversal of binary tree is")
#   printPostorder(root)

###**********print all leaf node ***************##
# class Node:
   
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
 
# # Function to print leaf
# # nodes from left to right
# def printLeafNodes(root: Node) -> None:
 
#     # If node is null, return
#     if (not root):
#         return
 
#     # If node is leaf node,
#     # print its data
#     if (not root.left and
#         not root.right):
#         print(root.data,
#               end = " ")
#         return
 
#     # If left child exists,
#     # check for leaf recursively
#     if root.left:
#         printLeafNodes(root.left)
 
#     # If right child exists,
#     # check for leaf recursively
#     if root.right:
#         printLeafNodes(root.right)
 
# # Driver Code
# if __name__ == "__main__":
 
#     # Let us create binary tree shown in
#     # above diagram
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.right.left = Node(5)
#     root.right.right = Node(8)
#     root.right.left.left = Node(6)
#     root.right.left.right = Node(7)
#     root.right.right.left = Node(9)
#     root.right.right.right = Node(10)
 
#     # print leaf nodes of the given tree
#     printLeafNodes(root)

###*****implement bfs and dfs ************##

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s, end = " ") 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')

# ##*********dfs*********##

# def dfs(node, graph, visited, component):
#     component.append(node)  # Store answer
#     visited[node] = True  # Mark visited

#     # Traverse to each adjacent node of a node
#     for child in graph[node]:
#         if not visited[child]:  # Check whether the node is visited or not
#             dfs(child, graph, visited, component)  # Call the dfs recursively


# if __name__ == "__main__":

#     # Graph of nodes
#     graph = {
#         0: [2],
#         1: [2, 3],
#         2: [0, 1, 4],
#         3: [1, 4],
#         4: [2, 3]
#     }
#     node = 0  # Starting node
#     visited = [False]*len(graph)  # Make all nodes to False initially
#     component = []
#     dfs(node, graph, visited, component)  # Traverse to each node of a graph
#     print(f"Following is the Depth-first search: {component}")

# ###***********sum of leaf node**********###

# class Node:
#     # Constructor to create a new Node
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
 
# # A utility function to check if a given node is leaf or not
# def isLeaf(node):
#     if node is None:
#         return False
#     if node.left is None and node.right is None:
#         return True
#     return False
 
# # This function return sum of all left leaves in a
# # given binary tree
# def leftLeavesSum(root):
 
#     # Initialize result
#     res = 0
     
#     # Update result if root is not None
#     if root is not None:
 
#         # If left of root is None, then add key of
#         # left child
#         if isLeaf(root.left):
#             res += root.left.key
#         else:
#             # Else recur for left child of root
#             res += leftLeavesSum(root.left)
 
#         # Recur for right child of root and update res
#         res += leftLeavesSum(root.right)
#     return res
 
# # Driver program to test above function
 
# # Let us construct the Binary Tree shown in the above function
# root = Node(20)
# root.left = Node(9)
# root.right = Node(49)
# root.right.left = Node(23)       
# root.right.right = Node(52)
# root.right.right.left = Node(50)
# root.left.left = Node(5)
# root.left.right = Node(12)
# root.left.right.right = Node(12)
# print ("Sum of left leaves is", leftLeavesSum(root))

###********sum of node of binary tree******************##

# def SumNodes(l):
     
#     # no of leaf nodes
#     leafNodeCount = pow(2, l - 1)
 
#     # list of vector to store nodes of
#     # all of the levels
#     vec = [[] for i in range(l)]
 
#     # store the nodes of last level
#     # i.e., the leaf nodes
#     for i in range(1, leafNodeCount + 1):
#         vec[l - 1].append(i)
 
#     # store nodes of rest of the level
#     # by moving in bottom-up manner
#     for i in range(l - 2, -1, -1):
#         k = 0
 
#         # loop to calculate values of parent nodes
#         # from the children nodes of lower level
#         while (k < len(vec[i + 1]) - 1):
 
#             # store the value of parent node as
#             # Sum of children nodes
#             vec[i].append(vec[i + 1][k] +
#                           vec[i + 1][k + 1])
#             k += 2
 
#     Sum = 0
 
#     # traverse the list of vector
#     # and calculate the Sum
#     for i in range(l):
#         for j in range(len(vec[i])):
#             Sum += vec[i][j]
 
#     return Sum
 
# # Driver Code
# if __name__ == '__main__':
#     l = 3
 
#     print(SumNodes(l))

####*************count subtree *************###

# class getNode:
#     def __init__(self, data):
 
#         # put in the data
#         self.data = data
#         self.left = self.right = None
 
# # function to count subtrees that
# # Sum up to a given value x
 
 
# def countSubtreesWithSumX(root, count, x):
 
#     # if tree is empty
#     if (not root):
#         return 0
 
#     # Sum of nodes in the left subtree
#     ls = countSubtreesWithSumX(root.left,
#                                count, x)
 
#     # Sum of nodes in the right subtree
#     rs = countSubtreesWithSumX(root.right,
#                                count, x)
 
#     # Sum of nodes in the subtree
#     # rooted with 'root.data'
#     Sum = ls + rs + root.data
 
#     # if true
#     if (Sum == x):
#         count[0] += 1
 
#     # return subtree's nodes Sum
#     return Sum
 
# # utility function to count subtrees
# # that Sum up to a given value x
 
 
# def countSubtreesWithSumXUtil(root, x):
 
#     # if tree is empty
#     if (not root):
#         return 0
 
#     count = [0]
 
#     # Sum of nodes in the left subtree
#     ls = countSubtreesWithSumX(root.left,
#                                count, x)
 
#     # Sum of nodes in the right subtree
#     rs = countSubtreesWithSumX(root.right,
#                                count, x)
 
#     # if tree's nodes Sum == x
#     if ((ls + rs + root.data) == x):
#         count[0] += 1
 
#     # required count of subtrees
#     return count[0]
 
 
# # Driver Code
# if __name__ == '__main__':
 
#     root = getNode(5)
#     root.left = getNode(-10)
#     root.right = getNode(3)
#     root.left.left = getNode(9)
#     root.left.right = getNode(8)
#     root.right.left = getNode(-4)
#     root.right.right = getNode(7)
 
#     x = 7
 
#     print("Count =",
#           countSubtreesWithSumXUtil(root, x))

###*************find sum of subtree***********###
# from collections import deque
 
# # A binary tree node has data, pointer
# # to left child and a pointer to right
# # child
# class Node:
     
#     def __init__(self, key):
         
#         self.data = key
#         self.left = None
#         self.right = None
 
# # Function to find the maximum sum
# # of a level in tree
# # using level order traversal
# def maxLevelSum(root):
     
#     # Base case
#     if (root == None):
#         return 0
 
#     # Initialize result
#     result = root.data
     
#     # Do Level order traversal keeping
#     # track of number
#     # of nodes at every level.
#     q = deque()
#     q.append(root)
     
#     while (len(q) > 0):
         
#         # Get the size of queue when the
#         # level order traversal for one
#         # level finishes
#         count = len(q)
 
#         # Iterate for all the nodes in
#         # the queue currently
#         sum = 0
#         while (count > 0):
             
#             # Dequeue an node from queue
#             temp = q.popleft()
 
#             # Add this node's value to current sum.
#             sum = sum + temp.data
 
#             # Enqueue left and right children of
#             # dequeued node
#             if (temp.left != None):
#                 q.append(temp.left)
#             if (temp.right != None):
#                 q.append(temp.right)
                 
#             count -= 1   
 
#         # Update the maximum node count value
#         result = max(sum, result)
 
#     return result
     
# # Driver code
# if __name__ == '__main__':
     
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(8)
#     root.right.right.left = Node(6)
#     root.right.right.right = Node(7)
   
#     print("Maximum level sum is", maxLevelSum(root))


###*************print node of odd level*********####
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    # If empty tree
    if (root == None):
        return
 
    # If current node is of odd level
    if (isOdd):
        print(root.data, end = " ")
 
    # Recur for children with isOdd
    # switched.
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root) 
 