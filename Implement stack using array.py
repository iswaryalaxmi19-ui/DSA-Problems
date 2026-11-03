class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        
    
    def is_empty(self):
        return len(self.stack) == 0