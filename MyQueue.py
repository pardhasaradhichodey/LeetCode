class MyQueue:

    def __init__(self):
        self.a=[]
        return None

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if self.a:
            temp=self.a[0]
            del self.a[0]
            return temp
        else:
            return None


    def peek(self) -> int:
        if self.a:
            return self.a[0]

    def empty(self) -> bool:
        if self.a:
            return False
        else:
            return True