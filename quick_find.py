class QuickFind:

    def __init__(self, size):
        self.id = [i for i in range(size)]
    
    def union(self, n, m):
        p = self.id[n]
        q = self.id[m]
        for i in range(len(self.id)):
            if self.id[i] == q:
                self.id[i] = p

    def connected(self, n, m):
        return self.id[n] == self.id[m]

size = int(input("size : "))            
uf = QuickFind(size)    
while True:
    n = int(input("n : "))
    if n == "q": break
    m = int(input("m : "))
    if not(uf.connected(n, m)):
        uf.union(n, m)
        print(n , m)
