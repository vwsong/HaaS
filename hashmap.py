class Hashmap:

    def __init__(self, size):
        self.size = size
        self.items = 0
        self.map = [[] for i in range(size)]

    def set(self, key, value):
        if self.size == self.items:
            return False

        hashed = hash(key)
        idx = hashed % self.size
        bucket = self.map[idx]
        self.items += 1

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True

        bucket.append((key, value))
        return True

    def get(self, key):
        hashed = hash(key)
        idx = hashed % self.size
        bucket = self.map[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v

        return None

    def delete(self, key):
        hashed = hash(key)
        idx = hashed % self.size
        bucket = self.map[idx]
        output = None

        for i, (k, v) in enumerate(bucket):
            if k == key:
                output = bucket.pop(i)
                self.items -= 1

        return output

    def load(self):
        return (self.items)/float(self.size)
