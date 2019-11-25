"""
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def make_ll(list):
	nodes = [ListNode(x) for x in list]
	for i in range(0, len(list) - 1):
		nodes[i].next = nodes[i + 1]
	return nodes[0]

def get_ll(linked_list):
	list = []
	while linked_list:
		list.append(linked_list.val)
		linked_list = linked_list.next
	return list

# class Solution(object):
# 	def reverseList_recurse(self, head, old):
# 		if old is None:
# 			return head
# 		tmp = old
# 		old = old.next
# 		tmp.next = head
# 		head = tmp
# 		return self.reverseList_recurse(head, old)

# 	def reverseList(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		return self.reverseList_recurse(None, head)

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		new, head = head, head.next
		new.next = None
		while head:
			tmp = head.next
			head.next = new
			new = head
			head = tmp
		return new

if __name__ == "__main__":
	s = Solution()
	ll_0 = make_ll([1, 2, 3, 4, 5])
	ex_0 = s.reverseList(ll_0)
	if get_ll(ex_0) != [5, 4, 3, 2, 1]:
		print("ERROR")
	ll_1 = make_ll([5, 4, 3, 2, 1])
	ex_1 = s.reverseList(ll_1)
	if [1, 2, 3, 4, 5] != get_ll(ex_1):
		print("ERROR")
	pass