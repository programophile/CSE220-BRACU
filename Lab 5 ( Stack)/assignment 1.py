class Stack:
    def __init__(self,length):
        self.array=[0]*length
        self.size=0
        self.length=length
    def is_full(self):
        if self.length==self.size:
            return True
        return False
    def is_empty(self):
        if self.size==0:
            return True
        return False
    def push(self,element):
        if self.is_full():
            return "Overflow"

        self.array[self.size]=element
        self.size+=1
    def pop(self):
        if self.is_empty():
            return "Under Flow"
        temp=self.array[self.size-1]
        self.array[self.size-1]=0
        self.size-=1
        return temp
    def peak(self):
        if self.is_empty():
            return "Under Flow"
        return self.array[self.size-1]
class parenthesisbalancing:
    def __init__(self,str1):
        self.input=str1
        self.lent=0
        for i in range(len(self.input)):
            if self.input[i]=="(" or "[" or "{" or ")" or "}" or "]":
                self.lent+=1
        self.stack= Stack(self.lent)
        self.index_stack=Stack(self.lent)
    def balancing(self):
        for i in range(len(self.input)):
            if self.input[i] == "(" or self.input[i] == "[" or self.input[i] == "{":
                self.stack.push(self.input[i])
                self.index_stack.push(i)
            else:
                if self.input[i]==")":
                    if self.stack.peak()=="(":
                        self.stack.pop()
                        self.index_stack.pop()
                    else:
                        print(f"worng , ( not closed , error at {self.index_stack.peak()+1} charecter")
                        break

                elif self.input[i]=="]":
                    if self.stack.peak()=="[":
                        self.stack.pop()
                        self.index_stack.pop()
                    else:
                        print(f"worng , {self.stack.peak()}not closed , error at {self.index_stack.peak()+1} charecter")
                        return
                elif self.input[i]=="}":
                    if self.stack.peak()=="{":
                        self.stack.pop()
                        self.index_stack.pop()
                    else:
                        print(f"worng , ) not closed , error at {self.index_stack.peak()+1} charecter")
                        break
        print("correcxt")
str1="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
a= parenthesisbalancing(str1)
a.balancing()

