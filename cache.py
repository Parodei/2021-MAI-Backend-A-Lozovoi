
class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.data = dict()
        self.data.items()

    def get(self, key: str) -> str:
        empty = ''
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value  
            return value
        else:
            return empty

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.data.pop(key)
        if len(self.data) >= self.capacity:
            self.data.popitem(last=False)
        self.data[key] = value

    def rem(self, key: str) -> None:
            self.data.pop(key)


from cache import LRUCache

cache = LRUCache(100)
#print(cache)
print(cache.set('Jesse', 'Pinkman'))
print(cache.set('Walter', 'White'))
print(cache.set('Jesse', 'James'))
print(cache.get('Jesse') )# вернёт 'James')
print(cache.rem('Walter'))
print(cache.get('Walter')) # вернёт ''