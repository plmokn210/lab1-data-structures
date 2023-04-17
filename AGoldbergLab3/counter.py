class Counter:
    def __init__(self, iterable):
        self.counts = {}
        for item in iterable:
            if item not in self.counts:
                self.counts[item] = 1
            else:
                self.counts[item] += 1
    
    def items(self):
        return self.counts.items()
    
    def keys(self):
        return self.counts.keys()
    
    def values(self):
        return self.counts.values()
    
    def __getitem__(self, key):
        return self.counts.get(key, 0)
    
    def __len__(self):
        return len(self.counts)
