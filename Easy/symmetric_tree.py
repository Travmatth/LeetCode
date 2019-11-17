"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# if parent is index i
# left child is 2*i + 1 and right child is 2*i + 2
def make_tree(list):
	n = len(list)
	tree_nodes = [(TreeNode(i) if i else None) for i in list]
	for i in range(n):
		left_i = 2 * i + 1
		right_i = 2 * i + 2
		if left_i < n:
			tree_nodes[i].left = tree_nodes[left_i]
		if right_i < n:
			tree_nodes[i].right = tree_nodes[right_i]
	return tree_nodes[0]

class Solution(object):
	def isMirror(self, left, right):
		"""
		:type left: TreeNode
		:type right: TreeNode
		:rtype: bool
		"""
		if not left and not right:
			return True
		elif not left or not right or left.val != right.val:
			return False
		outer = self.isMirror(left.left, right.right)
		both = outer and self.isMirror(left.right, right.left)
		return  both

	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		return self.isMirror(root.left, root.right)

	def isSymmetric_iter(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		queue = []
		queue.append(root)
		queue.append(root)
		while len(queue):
			left = queue.pop(0)
			right = queue.pop(0)
			if not left and not right:
				continue
			elif not left or not right:
				return False
			elif left.val != right.val:
				return False
			queue.append(left.left)
			queue.append(right.right)
			queue.append(left.right)
			queue.append(right.left)
		return True


if __name__ == "__main__":
	s = Solution()
	tree_0 = make_tree([1, 2, 2, 3, 4, 4, 3])
	ex_0 = s.isSymmetric_iter(tree_0)
	if ex_0 != True:
		print("ERROR")
	tree_1 = make_tree([1, 2, 2, None, 3, None, 3])
	ex_1 = s.isSymmetric_iter(tree_1)
	if ex_1 != False:
		print("ERROR")
