"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.
Given linked list -- head = [4,5,1,9], which looks like following:
Note:
    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.
"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		while node.next and node.next.next:
			node.val = node.next.val
			node = node.next
		node.val = node.next.val
		node.next = None

def make_ll(list):
	nodes = [ListNode(x) for x in list]
	for i in range(len(list) - 1):
		nodes[i].next = nodes[i + 1]
	return nodes[0]

def get_ll(ll):
	list = []
	while ll:
		list.append(ll.val)
		ll = ll.next
	return list

if __name__ == "__main__":
	s = Solution()
	ll_0 = make_ll([4,5,1,9])
	s.deleteNode(ll_0.next)
	ans_0 = get_ll(ll_0)
	if ans_0 != [4, 1, 9]:
		print("ERROR")
	# Explanation: You are given the second node with value 5
	# the linked list should become 4 -> 1 -> 9 after calling your function.
	ll_1 = make_ll([4,5,1,9])
	s.deleteNode(ll_1.next.next)
	ans_1 = get_ll(ll_1)
	if ans_1 != [4, 5, 9]:
		print("ERROR")
	# Explanation: You are given the third node with value 1, the linked
	# list should become 4 -> 5 -> 9 after calling your function.
	pass