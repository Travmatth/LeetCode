"""
Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).
"""

import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out, stack = [], [root]
        while len(stack):
            lvl, nxt = [], []
            for node in stack:
                if node:
                    lvl.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            if len(lvl):
                out.append(lvl)
            stack = nxt
        return out

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

if __name__ == "__main__":
    s = Solution()
    t_0 = make_tree([3, 9, 20, None, None, 15, 7])
    ex_0 = s.levelOrder(t_0)
    if ex_0 != [[3], [9,20], [15,7]]:
        print("Error")
    # Given binary tree ,
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    # [[3], [9,20], [15,7]]
    t_1 = stringToTreeNode("[1,2,3,4,null,null,5]")
    ex_1 = s.levelOrder(t_1)
    if ex_1 != [[3], [9,20], [15,7]]:
        print("Error")
    t_2 = stringToTreeNode("[1,2,null,3,null,4,null,5]")
    ex_2 = s.levelOrder(t_2)
    if ex_2 != [[3], [9,20], [15,7]]:
        print("Error")
    pass