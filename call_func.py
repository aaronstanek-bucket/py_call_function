def call_func(f,*a,**b):
    # f is a reference to a function
    ret = f(*a,**b)
    return ret

def call_method(obj,m,*a,**b):
    # obj is any object
    # m is a string refering to a method of that object
    f = getattr(obj,m)
    ret = f(*a,**b)
    return ret
