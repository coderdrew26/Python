class Multiset:
    def __init__(self)
        self.M=[]
        
    def add(self, val):
        self.M.append(val)
        
    def remove(self, val):
        if len(self.M):
            if val in self.M:
                self.M.remove(val)
        
    def __contain__(self, val):
        if val in self.M:
            return True
        return False

    def __len__(self):
        return len(self.M)