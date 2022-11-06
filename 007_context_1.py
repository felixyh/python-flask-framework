class Foo(object):

    def do_something(self):
        print(123)

    def close(self):
        pass


# 使用上下文管理类来管理其他类
class Context():
    def __enter__(self):
        self.data = Foo()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.close()

with Context() as ctx:
    ctx.do_something() 


