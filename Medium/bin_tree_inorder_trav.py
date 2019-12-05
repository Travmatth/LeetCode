"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

def make_tree(list):
    n = len(list)
    nodes = [(TreeNode(x) if x else None) for x in list]
    for i in range(n):
        if nodes[i] and 2 * i + 1 < n:
            nodes[i].left = nodes[(2 * i) + 1] 
        if nodes[i] and 2 * i + 2 < n:
            nodes[i].right = nodes[(2 * i) + 2] 
    return nodes[0]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recursive_inorder(self, root, out):
        if not root:
            return
        if root.left:
            self.recursive_inorder(root.left, out)
        out.append(root.val)
        if root.right:
            self.recursive_inorder(root.right, out)

    def iter_inorder(self, root, out):
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif len(stack):
                root = stack.pop()
                out.append(root.val)
                root = root.right
            else:
                break

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        # self.recursive_inorder(root, out)
        self.iter_inorder(root, out)
        return out

if __name__ == "__main__":
    s = Solution()
    t_0 = make_tree([1, None, 2, None, None, 3, None, None])
    ex_0 = s.inorderTraversal(t_0)
    if ex_0 != [1, 3, 2]:
        print("Error")
    t_1 = make_tree([1, 2, 3, 4, 5, 6, 7])
    ex_1 = s.inorderTraversal(t_1)
    if ex_1 != [4, 2, 5, 1, 6, 3, 7]:
        print("Error")
    pass