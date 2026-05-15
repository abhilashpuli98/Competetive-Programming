# Last Updated: 5/15/2026, 11:12:50 PM
MOD=(10**9+7)
class Fancy:
    def __init__(self):
        self.sequence=[]
        self.mul=1
        self.add=0

    def append(self, val: int) -> None:
        inv = pow(self.mul,MOD-2,MOD)
        base = (val-self.add)*inv%MOD
        self.sequence.append(base)

    def addAll(self, inc: int) -> None:
        self.add=(self.add+inc)%MOD

    def multAll(self, m: int) -> None:
        self.mul=self.mul*m%MOD
        self.add = self.add*m%MOD

    def getIndex(self, idx: int) -> int:
        if idx>=len(self.sequence):
            return -1
        return (self.sequence[idx]*self.mul+self.add)%MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)