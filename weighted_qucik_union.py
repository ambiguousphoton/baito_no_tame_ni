class QuickFind():
    def __init__(self, size):
        self.array = [i for i in range(size)]
        self.sizeOfComp = [1 for i in range(size)]

    def root(self, n) -> int:
        while n != self.array[n]:
            n = self.array[n]
        return n

    def union(self, n, m):
        if n == m : return 
        root1 = self.root(n)
        root2 = self.root(m)
        if root1 == root2:return 
        if (self.sizeOfComp[root1] < self.sizeOfComp[root2]):
            self.array[root1] = root2
            self.sizeOfComp[root2] += self.sizeOfComp[root1]
        else: 
            self.array[root2] = root1
            self.sizeOfComp[root1] += self.sizeOfComp[root2]

    def Connected(self, n, m) -> bool:
        return self.root(n) == self.root(m)

    def print(self):
        print(self.array)    

# input api
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