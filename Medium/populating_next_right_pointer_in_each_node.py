"""
You are given a perfect binary tree where all leaves are on
the same level, and every parent has two children. The
binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be
set to NULL.
Initially, all next pointers are set to NULL.
Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space
does not count as extra space for this problem.
Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def make_tree(list):
    nodes = [Node(i) for i in list]
    for i in range(len(list) - 1):
        if 2 * i + 1 >= len(list):
            break
        nodes[i].left = nodes[2 * i + 1]
        nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        stack = [root]
        while len(stack):
            nxt = []
            for node in stack:
                if node:
                    nxt.append(node.left)
                    nxt.append(node.right)
            if len(nxt):
                for i in range(len(nxt) - 1):
                    nxt[i].next = nxt[i + 1]
            stack = nxt
        return root

if __name__ == "__main__":
    s = Solution()
    t_0 = make_tree([1,2,3,4,5,6,7])
    ex_0 = s.connect(t_0)
    # Output: [1,#,2,3,#,4,5,6,7,#]
    # Explanation: Given the above perfect binary tree (Figure A), your function
    # should populate each next pointer to point to its next right node, just
    # like in Figure B. The serialized output is in level order as connected
    # by the next pointers, with '#' signifying the end of each level.
    pass