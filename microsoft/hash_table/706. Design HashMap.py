class hashmap:

    def __init__(self):
        self.d = {}

    def put(self,key,val):
        if key not in self.d:
            self.d[key] = val
        else:
            self.d[key] = val
    
    def get(self, key):
        if key not in self.d:
            return False
        return self.d[key]

    def remove(self, key):
        if key in self.d:
            del self.d[key]


cl = hashmap()
print(cl.func())