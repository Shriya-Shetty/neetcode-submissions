# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # global maximum

        def helper(node):
            if not node:
                return 0

            # compute max gain from left and right, ignore negatives
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)

            # path through this node
            current_path = node.val + left_gain + right_gain

            # update global max
            self.max_sum = max(self.max_sum, current_path)

            # return max gain if we continue path upwards
            return node.val + max(left_gain, right_gain)

        helper(root)
        return self.max_sum
