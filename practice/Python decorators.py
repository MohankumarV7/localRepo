#  What are Python decorators? Write one example

"a function which can change the functionaliy or behaviour of a original function without modifying its"
"source code. basically its takes function as an argument and returns a new funciton by modifying the original "
"function"

def logger(func):
    def wrapper(*args, **kwargs):
        print("func_called",func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logger
def process():
    print("processing...")

process()