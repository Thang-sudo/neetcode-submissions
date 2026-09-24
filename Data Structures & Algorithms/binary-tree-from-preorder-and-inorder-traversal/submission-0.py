# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def build(self, left: int, right: int, preorder: List[int], inorder: List[int], inorderMap: {}) -> Optional[TreeNode]:
        if left > right:
            return None
        preorderValue = preorder[self.preIndex]
        # Construct the root node of the tree
        rootNode = TreeNode(preorderValue)
        # Increment the preorder index to consume the next node
        self.preIndex += 1
        # Get the index of that root node to find the left and right subtree
        rootIndex = inorderMap[preorderValue]
        # Construct the left and right sub tree where 
        # in in order, 0 -> rootIndex is the left sub tree and rootIndex -> n - 1 is the right subtree
        rootNode.left = self.build(left, rootIndex - 1, preorder, inorder, inorderMap)
        rootNode.right = self.build(rootIndex + 1, right, preorder, inorder, inorderMap)
        # return root node after building its tree
        return rootNode
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIndex = 0
        inorderMap = {}
        # Map inorder values to its index for looking up
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        rootIndex = inorderMap[preorder[0]]
        # Initialize the root node of the tree and start building from here
        rootNode = TreeNode(preorder[0])
        
        return self.build(0, len(preorder) - 1, preorder, inorder, inorderMap)
        
