class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.pre = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.freq_lists = {}
        self.min_freq = 0

    def remove(self, node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    def insert(self, node):
        freq = node.freq

        if freq not in self.freq_lists:
            left = Node()
            right = Node()
            left.next = right
            right.pre = left
            self.freq_lists[freq] = (left, right)

        left, right = self.freq_lists[freq]

        pre = right.pre
        pre.next = node
        node.pre = pre
        node.next = right
        right.pre = node

    def increase_freq(self, node):
        freq = node.freq
        left, right = self.freq_lists[freq]

        self.remove(node)

        if left.next is right:
            del self.freq_lists[freq]

            if self.min_freq == freq:
                self.min_freq = freq + 1

        node.freq += 1
        self.insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.increase_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.increase_freq(node)
            return

        if len(self.cache) == self.capacity:
            left, right = self.freq_lists[self.min_freq]

            lfu = left.next
            self.remove(lfu)
            del self.cache[lfu.key]

            if left.next is right:
                del self.freq_lists[self.min_freq]

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)