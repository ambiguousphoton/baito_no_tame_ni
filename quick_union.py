class QuickFind():
    def __init__(self, size):
        self.array = [i for i in range(size)]
    
    def root(self, n) -> int:
        while n != self.array[n]:
            n = self.array[n]
        return n

    def union(self, n, m):
        rootIndex = self.root(n)
        self.array[rootIndex] = self.root(m)
    
    def Connected(self, n, m) -> bool:
        return self.root(n) == self.root(m)

    def print(self):
        print(self.array)    

size = int(input("size : "))            
uf = QuickFind(size)    

while True:
    n = int(input("n : "))
    if n == "q": break
    m = int(input("m : "))
    p = input("?? -> ")
    if p == "print":
        uf.print()
    if not(uf.Connected(n, m)):
        uf.union(n, m)
        print(n , m)