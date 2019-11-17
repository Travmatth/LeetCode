"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

def level_order_traversal(root, list):
	if not root:
		return
	q = [root]
	while True:
		node = q.pop(0)
		if not node and len(q):
			list.append(None)
		else:
			if not node and not len(q):
				break
			list.append(node.val)
			if node.left or q[0]:
				q.append(node.left)
			if node.right or q[0]:
				q.append(node.right)

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		n = len(nums)
		if n == 0 or n == 1:
			return None if not n else TreeNode(nums[0])
		mid = n // 2
		root = TreeNode(nums[mid])
		left, right = nums[:mid], nums[mid + 1:]
		root.left = self.sortedArrayToBST(left)
		root.right = self.sortedArrayToBST(right)
		return root


if __name__ == "__main__":
	s = Solution()
	ex_0 = s.sortedArrayToBST([-10, -3, 0, 5, 9])
	ans_0 = []
	level_order_traversal(ex_0, ans_0)
	if ans_0 != [0, -3, 9, -10, None, 5]:
		print("ERROR")