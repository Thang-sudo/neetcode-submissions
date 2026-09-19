# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Basically, find the most outer node at each level
        # Think about BST when dealing with level order
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                if i == size - 1:
                    result.append(current.val)
        
        return result
