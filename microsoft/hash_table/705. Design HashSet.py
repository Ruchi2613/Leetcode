class Hashset:

    def __init__(self):
        self.list1 = []

    def add(self,key):
        if key not in self.list1:
            self.list1.append(key)
    
    def remove(self,key):
        if key in self.list1:
            self.list1.remove(key)
        

    def contains(self,key):
        return key in self.list1
cl = Hashset()
print(cl.func())