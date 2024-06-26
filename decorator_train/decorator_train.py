def error_handler_decorator(fn):
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            return result
        except Exception as e:
            print("ERROR: ", e)
    return wrapper

@error_handler_decorator
def sum(int1,int2):
    print (int(int1)+int(int2))
@error_handler_decorator
def minus(int1,int2):
    return int1- int2

print(sum(1,2))
print(sum(0,['dsa']))

