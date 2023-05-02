class ArrayQueue:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=0
        self.front=0
        self.back=0
    def enqueue(self,elem):
        if self.size==len(self.queue):
            print("Overflow")
        else:
            self.queue[self.back]=elem
            self.back=(self.back+1)%len(self.queue)
            self.size+=1
    def dequeue(self):
        if self.size==0:
            print("Underflow")
        else:
            d_item=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%len(self.queue)
            self.size-=1
            return d_item
    def peek(self):
        if self.size==0:
            print("Overflow")
        else:
            return self.queue[self.front]
