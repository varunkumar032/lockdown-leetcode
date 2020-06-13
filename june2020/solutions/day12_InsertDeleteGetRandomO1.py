# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

# Example:
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

import random
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dictionary = {}

    def insert(self, val):
        if val in self.dictionary:
            return False
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val in self.dictionary:
            deleteIndex = self.dictionary[val]
            self.dictionary[self.list[-1]] = deleteIndex
            del self.dictionary[val]
            self.list[deleteIndex] = self.list[-1]
            self.list.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.list)
