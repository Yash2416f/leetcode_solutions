# leetcode 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/

class MyStack:

    def __init__(self):
        self.sta=[]

    def push(self, x: int) -> None:
        self.sta.append(x)


    def pop(self) -> int:
        return self.sta.pop()
        

    def top(self) -> int:
        return self.sta[-1]

    def empty(self) -> bool:
        return len(self.sta)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()