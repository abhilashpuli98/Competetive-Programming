# Last Updated: 5/15/2026, 11:14:44 PM
class StockSpanner:

    def __init__(self):
        self.pstack=[]
        self.sstack=[]

    def next(self, price: int) -> int:
        span=1
        while self.pstack and self.sstack and self.pstack[-1]<=price:
            span+=self.sstack[-1]
            self.pstack.pop()
            self.sstack.pop()
        self.pstack.append(price)
        self.sstack.append(span)
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)