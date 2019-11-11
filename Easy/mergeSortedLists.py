"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode(object):
	def __init__(self, x, next = None):
		self.val = x
		self.next = next

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not l1 or not l2:
			return l2 if not l1 else l1
		out = ListNode(0)
		last = out
		while l1 and l2:
			lesser = None
			if l1.val < l2.val:
				lesser  = l1
				l1 = l1.next
			elif l1.val >= l2.val:
				lesser  = l2
				l2 = l2.next
			last.next = lesser
			last = last.next
		last.next = l1 if l1 else l2
		return out.next 

if __name__ == "__main__":
	s = Solution()
	n_0 = ListNode(1, ListNode(2, ListNode(3)))
	n_1 = ListNode(1, ListNode(2, ListNode(3)))
	n_2 = ListNode(2, ListNode(3, ListNode(4)))
	n_3 = ListNode(4, ListNode(5, ListNode(6)))

	ex_0 = s.mergeTwoLists(None, None)
	ex_1 = s.mergeTwoLists(None, n_0)
	ex_2 = s.mergeTwoLists(ex_1, None)
	ex_3 = s.mergeTwoLists(ex_2, n_1)
	ex_4 = s.mergeTwoLists(ex_3, n_2)
	ex_5 = s.mergeTwoLists(n_3, ex_4)
