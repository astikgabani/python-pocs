"""
Whenever we need to compare a lot of strings. We can use the interning concepts of python.

::::: OUTPUT :::::

$ python string_interning.py 
---------------------------------------
simple_string comparison
time : 13.766726799999999
---------------------------------------
interning string comparison
time : 0.7635757999999999
---------------------------------------

"""

import sys
import time


def string_compare_simple(n):
    a = "Hey there, this is testing string" * 300
    b = "Hey there, this is testing string" * 300
    for _ in range(n):
        if a == b:
            pass


def string_compare_with_interning(n):
    a = sys.intern("Hey there, this is testing string" * 300)
    b = sys.intern("Hey there, this is testing string" * 300)
    for _ in range(n):
        if a is b:
            pass


print("---------------------------------------")
print("simple_string comparison")
start = time.perf_counter()
string_compare_simple(10000000)
end = time.perf_counter()
print(f"time : {end-start}")

print("---------------------------------------")
print("interning string comparison")
start = time.perf_counter()
string_compare_with_interning(10000000)
end = time.perf_counter()
print(f"time : {end-start}")
print("---------------------------------------")
