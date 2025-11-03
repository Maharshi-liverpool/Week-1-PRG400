class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B): 
    pass

obj = C()
obj.greet()

#Explain: Since class C inherits from A first, Python uses Method Resolution Order (MRO).
#So the greet() method from A is called first.