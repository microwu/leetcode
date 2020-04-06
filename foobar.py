import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = threading.Lock()
        self.lockBar = threading.Lock()
        threadFoo = threading.Thread(target=self.foo,args=(lambda : print("foo",end=''),))
        threadBar = threading.Thread(target=self.bar,args=(lambda : print("bar",end=''),))
        self.lockBar.acquire()
        threadFoo.start()
        threadBar.start()
        threadFoo.join()
        threadBar.join()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lockFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lockBar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            self.lockBar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lockFoo.release()

if __name__ == '__main__':
    foobar = FooBar(2)
    # foobar.foo(lambda : print("foo",end=''))
    # foobar.bar(lambda : print("bar",end=''))

