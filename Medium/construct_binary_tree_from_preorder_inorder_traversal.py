"""
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    in preorder, leftmost element is root
    in inorder, elements to left of root are children on left side
              , elements to right of root are children on right side
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not len(inorder):
            return None
        i = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        l_pre, l_inorder   = preorder[1:], inorder[:i]
        root.left = self.buildTree(l_pre, l_inorder)
        r_pre, r_inorder = preorder[i + 1:], inorder[i + 1:]
        root.right = self.buildTree(r_pre, r_inorder)
        return root

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    #   3
    #  / \
    # 9  20
    #   /  \
    #  15   7
    pass