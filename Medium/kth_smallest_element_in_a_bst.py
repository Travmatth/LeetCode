"""
Given a binary search tree, write a function
kthSmallest to find the kth smallest element in it.
Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Follow up:
What if the BST is modified (insert/delete operations) often
and you need to find the kth smallest frequently? How would
you optimize the kthSmallest routine?
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
    def preorder(self, root, k, stack):
        if not root:
            return
        self.preorder(root.left, k, stack)
        if len(stack) == k:
            return
        stack.append(root.val)
        self.preorder(root.right, k, stack)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        self.preorder(root, k, stack)
        return stack[-1]

if __name__ == '__main__':
    s = Solution()
    t_0 = stringToTreeNode('[3,1,4,null,2]')
    ex_0 = s.kthSmallest(t_0, 1)
    if ex_0 != 1:
        print("Error")
    #   3
    #  / \
    # 1   4
    #  \
    #   2
    t_1 = stringToTreeNode('[5,3,6,2,4,null,null,1]')
    ex_1 = s.kthSmallest(t_1, 3)
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    if ex_1 != 3:
        print("Error")
    pass