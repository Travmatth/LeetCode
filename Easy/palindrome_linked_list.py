"""
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def make_ll(list):
	nodes = [ListNode(x) for x in list]
	for i in range(len(nodes) - 1):
		nodes[i].next = nodes[i + 1]
	return nodes[0]

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head:
			return True
		stack, ll = [], head
		while ll:
			stack.append(ll.val)
			ll = ll.next
		while head and len(stack):
			if head.val != stack.pop():
				return False
			head = head.next
		return True if not head and len(stack) == 0 else False

if __name__ == "__main__":
	s = Solution()
	ll_0 = make_ll([1, 2])
	ex_0 = s.isPalindrome(ll_0)
	if ex_0 != False:
		print("Found")
	ll_1 = make_ll([1, 2, 2, 1])
	ex_1 = s.isPalindrome(ll_1)
	if ex_1 != True:
		print("Found")
	pass