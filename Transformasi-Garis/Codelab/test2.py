def uppercase_decorator(function):
    def wrapper():
        func_result = function()
        uppercase_result = func_result.upper()
        print(uppercase_result)
        return uppercase_result
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()