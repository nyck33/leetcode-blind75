'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            # Base case: node is None
            if not node:
                return 0
            
            # Get the maximum sum of the left subtree
            left_sum = max(dfs(node.left), 0)
            # Get the maximum sum of the right subtree
            right_sum = max(dfs(node.right), 0)
            
            # Update the maximum path sum so far with the sum of the current node
            # and the maximum sums of the left and right subtrees
            self.max_path_sum = max(self.max_path_sum, node.val + left_sum + right_sum)
            
            # Return the maximum sum of the current node and the maximum sum of its
            # left and right subtrees
            return node.val + max(left_sum, right_sum)
        
        # Initialize the maximum path sum to negative infinity
        self.max_path_sum = float('-inf')
        
        # Start the depth-first search
        dfs(root)
        
        # Return the maximum path sum
        return self.max_path_sum