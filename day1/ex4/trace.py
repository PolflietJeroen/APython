#!/usr/bin/encv python3

def not_none(f):
    def func(*args, **kwargs):
        if any(arg is None for arg in args):
            print('function {}: does not take arguments of None'.format(f.__name__))
            return 
        else:
            return f(*args, **kwargs)
    return func

def trace (func):
    def traced(*args, **kwargs):
        print ("Trace: {0} ({1}:{2})".format(func.__name__, func.__code__.co_filename, func.__code__.co_firstlineno))
        return func(*args, **kwargs)
    return traced
@trace
@not_none
def test(a, b):
    print (a, b)
@trace
@not_none
def bar(a):
    print ('nice')
@trace
@not_none
def foo(a):
    print ('test')
n = 3
foo(n)    
num = None
pre = 3
test(num, pre)
foo(n)
bar(n)
foo(num)
