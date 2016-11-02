#!/usr/bin/encv python3

# ITERATOR
#class Counter:
#    def __init__(self, low, high):
#        self.current = low
#        self.high = high
#        
#    def __iter__(self):
#        return self
#            
#    def __next__(self):
#        if self.current > self.high:
#            raise StopIteration
#        else:
#            self.current += 1
#            return self.current - 1
#
#for c in Counter(3,8):
#    print (c)

# GENERATOR
def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1


    
def fib(num):
    i = 0
    current, nex = 0, 1
    while i < num: 
        yield current
        current, nex = nex, current + nex
        i += 1    

#for c in counter(3, 8):
#    print (c)

for f in fib(8):
    print (f)
