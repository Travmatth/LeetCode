"""
Given a binary tree, return the zigzag level order traversal
of its nodes' values. (ie, from left to right, then right to
left for the next level and alternate between).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        i, out, stack = 0, [], [root]
        while len(stack):
            nxt, lvl = [], []
            for node in stack:
                if node:
                    lvl.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            if len(lvl):
                if i % 2:
                    lvl = [x for x in reversed(lvl)]
                out.append(lvl)
            i, stack = i + 1, nxt
        return out

if __name__ == "__main__":
    s = Solution()
    t_0 = stringToTreeNode("[3,9,20,null,null,15,7]")
    ex_0 = s.zigzagLevelOrder(t_0)
    if ex_0 != [[3], [20,9], [15,7]]:
        print("Error")
    t_1 = stringToTreeNode("[1,2,3,4,null,null,5]")
    ex_1 = s.zigzagLevelOrder(t_1)
    if ex_1 != [[1],[3,2],[4,5]]:
        print("Error")
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    pass