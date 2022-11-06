class Foo(object()):

    # with 调用的魔法函数， 返回值赋给as 的对象
    def __enter__(self):
        return 123

    # with 语法会自动关闭，调用的就是exit 魔法函数
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

obj = Foo()

with obj as f:
    print(f)