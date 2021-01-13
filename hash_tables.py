class HashTable:
    """ Hash table for strings using chaining with arrays """
    def __init__(self, length):
        self.values = {}
        self.length = length
        self.HASH_MAP = {"a": 1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,"i":9,"j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

    def __str__(self):
        print("Hash table of length{}: {}".format(self.length,self.values))

    def Hash(self, s):
        ind = 0
        for c in s: ind = ind + self.HASH_MAP[c]
        return str(ind % (self.length + 1))

    def Insert(self, s):
        ind = self.Hash(s)
        if ind in self.values: self.values[ind].append(s)
        else: self.values[ind] = [s] 

    def Search(self, s):
        ind = self.Hash(s)
        if ind in self.values:
            for ss in self.values[ind]: 
                if ss == s : return ind
            return -1
        else: return -1
    
    def Remove(self, s):
        ind = self.Search(s)
        if ind == -1: raise ValueError("String not in Hash")
        if len(self.values[ind]) == 1: del self.values[ind]
        else: 
            for i in range(len(self.values[ind])):
                if self.values[ind][i] == s: self.values[ind].pop(i)


hash_table = HashTable(4)

hash_table.Insert('hello')
hash_table.Insert('hi')
hash_table.Insert('goodbye')
hash_table.__str__()
hash_table.Remove('hi')
hash_table.__str__()