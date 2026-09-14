class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}          # stores key -> value
        self.capacity = capacity
        self.order = []         # track usage order (most recent at end)

    def get(self, key: int) -> int:
        if key in self.dict:
            # move key to end (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # update value and move to end
            self.dict[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.dict) == self.capacity:
                # evict least recently used (first in list)
                lru = self.order.pop(0)
                self.dict.pop(lru)
            # insert new key
            self.dict[key] = value
            self.order.append(key)
