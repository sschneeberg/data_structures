class Stack:
    """ This is a stack array implementation. Last In First Out """
    def __init__(self, values):
        self.values = values

    def isEmpty(self):
        """ Check if stack is empty """ 
        return True if len(self.values) == 0 else False

    def Peek(self):
        """ See next value """ 
        return "Empty" if self.isEmpty() else self.values[-1]

    def Push(self, n):
        """ Add new value """ 
        self.values.append(n)


    def Pop(self):
        """ Remove next value """ 
        return self.values.pop()


class Queue:
    """ This is a queue array implementation. First In First Out """
    def __init__(self, values):
        self.values = values

    def isEmpty(self):
        """ Check if stack is empty """ 
        return (len(self.values) == 0)

    def Peek(self):
        """ See next value """ 
        return  "Empty" if self.isEmpty() else self.values[0]
    
    def Enqueue(self, n):
        """ Add new value """
        self.values.append(n)

    def Dequeue(self):
        """ Remove next value """ 
        return self.values.pop(0)

queue = Queue([1,2,3,4])
stack = Stack([1,2,3,4])

print(queue.Peek())
print(stack.Peek())

print(queue.Dequeue())
print(stack.Pop())

queue.Enqueue(5)
stack.Push(5)

print(queue.Peek())
print(stack.Peek())