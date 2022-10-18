from functools import wraps

def auth(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@auth
def login():
    pass

print(login.__name__)
