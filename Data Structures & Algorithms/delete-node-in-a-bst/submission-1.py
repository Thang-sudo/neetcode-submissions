# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        # First need to find the right node to delete
        # if key larger than root val then node is in the right subtree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        # if key smaller than root val the node is in the left subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # if we find the key delete the node based on the 2 cases
        else:
            # if the root has 0 or 1 child
            # then check the remaining child and return
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                # find the node with min value of the right sub tree and replace its value with current root's value
                # This ensures that the replacing value still keeps the properties of BST
                # Delete that node with min value of the right sub tree
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root