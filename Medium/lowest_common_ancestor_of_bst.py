"""
Given a binary tree, find the lowest common ancestor
(LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two
nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be
a descendant of itself).
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist
in the binary tree.
"""

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if root.val < p and root.val < q:
                root = root.left
            elif root.val > p and root.val > q:
                root = root.right
            else:
                return root.val

if __name__ == '__main__':
    s = Solution()
    t_0 = stringToTreeNode('[3,5,1,6,2,0,8,null,null,7,4]')
    ex_0 = s.lowestCommonAncestor(t_0, 5, 1)
    if ex_0 != 3:
        print("Error")
    # Explanation: The LCA of nodes 5 and 1 is 3.
    t_1 = stringToTreeNode('[3,5,1,6,2,0,8,null,null,7,4]')
    ex_1 = s.lowestCommonAncestor(t_1, 5, 4)
    if ex_1 != 5:
        print("Error")
    # Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    pass