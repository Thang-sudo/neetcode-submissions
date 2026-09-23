# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        results = []
        results.extend([root.val])
        results.extend(self.preorderTraversal(root.left))
        results.extend(self.preorderTraversal(root.right))

        return results