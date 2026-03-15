class A:
    def __init__(self):
        print("A")
class B1(A):
    def __init__(self):
        super().__init__()
        
        print("我是B1")
class B2(A):
    def __init__(self):
        super().__init__()
        print("我是B2")
class C(B1,B2):
    def __init__(self):
        super().__init__()
        print("我是C")
