class RandomizedSet:

    def __init__(self):
        self.set = []
        self.map = {}


    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.map[val] = len(self.set)
        self.set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        else:
            index_remove = self.map[val]
            last_copy = self.set[-1]

            self.set[index_remove] = last_copy
            self.map[last_copy] = index_remove

            self.set.pop()
            del self.map[val]

            return True

        

    def getRandom(self) -> int:
        return random.choice(self.set)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()