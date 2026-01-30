class MyQueue(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        for i in range(len(self.stack)-1):
            self.stack.append(self.stack[-i])
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        
