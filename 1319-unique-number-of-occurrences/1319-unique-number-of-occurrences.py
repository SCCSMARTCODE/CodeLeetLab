class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        storage = dict()
        for x in arr:
            if x in storage.keys():
                storage[x] += 1
            else:
                storage.update({x: 1})
        values = storage.values()
        return len(values) == len(set(values))