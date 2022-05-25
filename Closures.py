def decorated_func(outer_func):
    def wrapper_func():
        return outer_func()
    return wrapper_func

def display():
    print('display function ran')

decorated=decorated_func(display)
decorated()