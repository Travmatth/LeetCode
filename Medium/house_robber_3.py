"""
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this
place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without
alerting the police.
Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

from typing import *

class TreeNode(object):
    def __init__(self, val):
        self.val = val
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

class Solution:
    def rob_recursive(self, root: TreeNode, can_rob: bool) -> int:
        if not root:
            return 0
        elif can_rob:
            robbed = root.val
            robbed += self.rob_recursive(root.left, False)
            robbed += self.rob_recursive(root.right, False)
            not_robbed = self.rob_recursive(root.left, True)
            not_robbed += self.rob_recursive(root.right, True)
            return max(robbed, not_robbed)
        else:
            not_robbed = self.rob_recursive(root.left, True)
            not_robbed += self.rob_recursive(root.right, True)
            return not_robbed

    def rob_memoized(self, root: TreeNode, can_rob: bool, memo: Dict[Any, int]) -> int:
        if not root:
            return 0
        elif can_rob and root in memo:
            return memo[root]
        elif can_rob:
            robbed = root.val
            robbed += self.rob_memoized(root.left, False, memo)
            robbed += self.rob_memoized(root.right, False, memo)
            not_robbed = self.rob_memoized(root.left, True, memo)
            not_robbed += self.rob_memoized(root.right, True, memo)
            memo[root] = max(robbed, not_robbed)
            return memo[root]
        else:
            not_robbed = self.rob_memoized(root.left, True, memo)
            not_robbed += self.rob_memoized(root.right, True, memo)
            return not_robbed

    def rob(self, root: TreeNode) -> int:
        # return self.rob_recursive(root, True)
        return self.rob_memoized(root, True, {})
        

if __name__ == "__main__":
    s = Solution()
    tree_0 = stringToTreeNode("[4,1,null,2,null,3]")#"[3,2,3,null,3,null,1]")
    """
         4
        /
       1
      /
     2
    /
   3
    """
    ex_0 = s.rob(tree_0)
    if ex_0 != 7:
        print("Error, ", ex_0)
    tree_1 = stringToTreeNode("[3,4,5,1,3,null,1]")
    ex_1 = s.rob(tree_1)
    if ex_1 != 9:
        print("Error, ", ex_1)
    pass