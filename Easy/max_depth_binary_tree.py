"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def make_tree(list):
	n = len(list)
	nodes = [(TreeNode(i) if i else None) for i in list]
	for i in range(n):
		left = 2 * i + 1
		right = 2 * i + 2
		if left < n:
			nodes[i].left = nodes[left]
		if right < n:
			nodes[i].right = nodes[right]
	return nodes[0]

class Solution(object):
	def getDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		left = 1 + self.getDepth(root.left) if root.left else 0 
		right = 1 + self.getDepth(root.right) if root.right else 0
		return left if left > right else right

	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		return 1 + self.getDepth(root)

if __name__ == "__main__":
	s = Solution()
	tree_1 = make_tree([3, 9, 20, None, None, 15, 7])
	ex_0 = s.maxDepth(tree_1)
	if ex_0 != 3:
		print("ERROR")