#leetcode problem 155: Minimum Stack
# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.sta=[]
        self.min_sta=[]

    def push(self, val: int) -> None:
        self.sta.append(val)
        if (len(self.min_sta)==0) or val<=self.min_sta[-1]:
            self.min_sta.append(val)

    def pop(self) -> None:
        if len(self.sta)==0:
            return 
        
        var=self.sta.pop()
        if self.min_sta[-1]==var:
            self.min_sta.pop()
        


    def top(self) -> int:
        if len(self.sta)==0:
            return
        else:
            return self.sta[-1]

    def getMin(self) -> int:
        if len(self.sta)==0:
            return 
        else:
            return self.min_sta[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()