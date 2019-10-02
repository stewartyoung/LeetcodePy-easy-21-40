class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []        

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x

        # append the tuple 
        self.q.append((x,curMin))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            self.q[len(self.q)-1][0]

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else: 
            return self.q[len(self.q)-1][1]