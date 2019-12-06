"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def is_valid(self, root, low, high):
        if not root:
            return True
        elif root.val <= low or root.val >= high:
            return False
        left = self.is_valid(root.left, low, root.val)
        return left and self.is_valid(root.right, root.val, high)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root, float('-inf'), float('inf'))

def make_tree(list):
    n = len(list)
    nodes = [(TreeNode(x) if x != None else None) for x in list]
    for i in range(n):
        if nodes[i] and 2 * i + 1 < n:
            nodes[i].left = nodes[(2 * i) + 1] 
        if nodes[i] and 2 * i + 2 < n:
            nodes[i].right = nodes[(2 * i) + 2] 
    return nodes[0]

if __name__ == "__main__":
    s = Solution()
    t_0 = make_tree([1, 1, None])
    ex_0 = s.isValidBST(t_0)
    if ex_0 != True:
        print("Error")
    # Example 1:
    #     2
    #    / \
    #   1   3
    t_1 = make_tree([5, 1, 4, None, None, 3, 6])
    ex_1 = s.isValidBST(t_1)
    if ex_1 != False:
        print("Error")
    # Example 2:
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    t_2 = make_tree([10, 5, 15, None, None, 6, 20])
    ex_2 = s.isValidBST(t_2)
    if ex_2 != False:
        print("Error")
    t_3 = make_tree([1, 1, None])
    ex_3 = s.isValidBST(t_3)
    if ex_3 != False:
        print("Error")
    pass