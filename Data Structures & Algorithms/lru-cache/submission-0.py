class Node:
    def __init__(self, key, val):
        self.key = key # Use key because when we want to delete a node from the linked list, we need to use the key and delete the key vaule pair from the map with O(1) time
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
    
    def remove(self, node: Node) -> None:
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.prev = node.next = None

    def insertHead(self, node) -> None:
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update the mode recently used key by putting it to the head of the linked list
            self.remove(self.cache[key])
            self.insertHead(self.cache[key])
            # Return the value of this node
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Check if key already in cache. If so, just update the value and update the most recently used key
        if key in self.cache:
            self.cache[key].val = value
        # Update the most recent node to be this one
            self.remove(self.cache[key])
            self.insertHead(self.cache[key])
        # else, we need to put key into the cache
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertHead(newNode)
            if self.size < self.capacity:
                self.size += 1
            else:
                # Need to remove the least used node
                leastUsedNode = self.tail.prev
                self.remove(leastUsedNode)
                del self.cache[leastUsedNode.key]
