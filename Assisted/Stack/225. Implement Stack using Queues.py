class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)== 0
        