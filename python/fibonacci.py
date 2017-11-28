#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci.py
#  

def fib_iter(n):
    a,b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        tmp = b
        a = tmp
        b = a + b
        print(a, "" , b, "", b/a)
    
        
    print() # wyraz odstępu
    return b

def main(args):
    n = int(input("Podaj nr wyrazu: " ))
    fib_iter(n)
    print()
    print("wyraz {:d} = {:d}".format(n, fib_iter(n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
