# Last Updated: 6/21/2026, 7:05:14 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.head=0
        self.queue=[0]*k
        self.cap=k
        self.count=0

    def enQueue(self, value: int) -> bool:
        if self.cap==self.count:
            return False
        self.queue[(self.head+self.count)%self.cap]=value
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.count==0:
            return False
        self.head=(self.head+1)%self.cap
        self.count-=1
        return True
    def Front(self) -> int:
        return self.queue[self.head] if self.count else -1

    def Rear(self) -> int:
        return self.queue[(self.head+self.count-1)%self.cap] if self.count else -1

    def isEmpty(self) -> bool:
        return self.count==0

    def isFull(self) -> bool:
        return self.count==self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()