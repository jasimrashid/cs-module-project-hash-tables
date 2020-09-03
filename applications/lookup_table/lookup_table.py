# from math import random
import random
import math as m
import time

def slowfun_too_slow(x, y):
    v = m.pow(x, y)
    v = m.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

vpow = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # factorial = {}
    # quotient = {}
    key_vpow = str(x)+'-'+str(y)
    if key_vpow not in vpow:
        temp = m.pow(x,y)
        temp = m.factorial(temp)
        temp //= (x+y)
        temp %= 982451653
        vpow[key_vpow] = temp
    
    return vpow[key_vpow]   
    
# Do not modify below this line!
"""
start_time = time.time()
for i in range(300):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
    print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
end_time = time.time()
print('time 1', end_time - start_time)
# 4.42 secs
# 300 --> 25s

"""

# breakpoint()


start_time = time.time()
for i in range(100000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
end_time = time.time()
print('time 2', end_time - start_time)
