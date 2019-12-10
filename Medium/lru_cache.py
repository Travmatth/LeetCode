"""
Design and implement a data structure for Least Recently Used
(LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the
    key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already
    present. When the cache reached its capacity, it should invalidate
    the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
Could you do both operations in O(1) time complexity?
"""

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current = 0
        self.hash = {}
        self.head = None
        self.tail = None

    def inc_recency(self, key):
        node = self.hash[key]
        if node == self.head:
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.inc_recency(key)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        at_capacity = self.current == self.capacity
        present = key in self.hash
        # swap recency
        if (at_capacity and present) or (not at_capacity and present):
            self.inc_recency(key)
            self.hash[key].val = value
        # evict old, set new
        elif at_capacity and not present:
            node = Node(key, value)
            tail = self.tail
            if self.capacity == 1:
                self.head = self.tail = node
            else:
                self.tail = tail.prev
                self.tail.next = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.hash[key] = node
            del self.hash[tail.key]
        # set new
        elif not at_capacity and not present:
            node = Node(key, value)
            if not self.head and not self.tail:
                self.head = self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.hash[key] = node
            self.current += 1

if __name__ == "__main__":
    # cache = LRUCache(4)
    # cache.put(4, 4)
    # cache.put(3, 3)
    # cache.put(2, 2)
    # cache.put(1, 1)
    # cache.put(0, 0)
    # cache.get(3)
    cache = LRUCache(1)
    cache.put(2,1)
    cache.get(2)
    cache.put(3,2)
    cache.get(2)
    cache.get(3)

    cache = LRUCache(10);
    fx = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    params = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    out = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,24,None,4,29,30,None,-1,-1,None,None,None,None,29,None,None,None,None,17,22,-1,None,None,None,-1,None,None,None,20,None,None,None,-1,-1,-1,None,None,None,None,20,None,None,None,None,None,None,None]
    expected = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
    for i in range(len(fx)):
        f, p, expect = fx[i], params[i], expected[i]
        actual = getattr(cache, f)(*p)
        if actual != expect:
            print("Error")
    pass