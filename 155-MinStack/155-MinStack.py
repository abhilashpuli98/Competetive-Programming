# Last Updated: 6/22/2026, 12:43:10 AM
class MinStack:

    def __init__(self):
        self.st=[]

    def push(self, val: int) -> None:
        curr=self.getMin()
        if curr is None or curr>val:
            curr=val
        self.st.append([val,curr])

    def pop(self) -> None:
        return self.st.pop() if self.st else None

    def top(self) -> int:
        return self.st[-1][0]if self.st else None
    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()