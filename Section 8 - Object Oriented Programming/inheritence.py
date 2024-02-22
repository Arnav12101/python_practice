class B:
    def __init(self):
        print('init of class B')

    def function2(self):
        print('this is function 2')


class A:
    def __init__(self):
        print('init of class A')
    
    def function1(self):
        print('this is function1')




class c(B, A):
    def __init__(self):
        super().__init__()

obj = c()
obj.function1()
obj.function2()