#!/usr/bin/env python3

'''
For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous two.

Further, we define DA,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.

Example:

Let A=1415926535, B=8979323846. We wish to find D_A,B(35), say.

The first few terms of FA,B are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846

Then D_A,B(35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510 
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128 
48111745028410270193852110555964462294895493038196 .

Find the sum_(n = 0,1,...,17)   10^n * D_A,B((127+19n)*7^n).
'''


def calc_simple():
    outstr = ''
    for n in range(0, 3):
        A = ('1415926535897932384626433' +
             '8327950288419716939937510' +
             '5820974944592307816406286' +
             '2089986280348253421170679')
        B = ('8214808651328230664709384' +
             '4609550582231725359408128' +
             '4811174502841027019385211' +
             '0555964462294895493038196')
    
        wanted = (127+19*n)*7**n

        a1 = 'A'
        a2 = 'B'
        a3 = a1 + a2

        limit = wanted//100
        while len(a3) < limit:
            a1 = a2
            a2 = a3
            a3 = a1 + a2
        if a3[limit] == 'A':
            real = A
        else:
            real = B
        outstr += real[wanted % 100 - 1]
    return outstr


def a_or_b(n):
    wanted = (127+19*n)*7**n
    values = calc_fib(wanted//100+1)
    i = len(values)-1
    while i > 2:
        if wanted//100 >= values[i-2]:
            wanted -= values[i-2]*100
            i -= 1
        else:
            i -= 2
    if wanted < 100 and i ==2:
        return 'A'
    else:
        return 'B'


def test_a_or_b():
    A = ('1415926535897932384626433' +
         '8327950288419716939937510' +
         '5820974944592307816406286' +
         '2089986280348253421170679')
    B = ('8214808651328230664709384' +
         '4609550582231725359408128' +
         '4811174502841027019385211' +
         '0555964462294895493038196')
    
    expected = calc_simple()
    for n in range(len(expected)):
        wanted = (127+19*n)*7**n
        if a_or_b(n) == 'A':
            real = A
        else:
            real = B
        assert (n, real[wanted % 100 + 1]) == (n, expected[n])
    n = 12


def calc_fib(limit):
    a1 = 1
    a2 = 1
    a3 = a1 + a2
    values = [a1, a2, a3]
    while a3 < limit:
        a1 = a2
        a2 = a3
        a3 = a1 + a2
        values.append(a3)
    return values


def main():
    A = ('1415926535897932384626433' +
         '8327950288419716939937510' +
         '5820974944592307816406286' +
         '2089986280348253421170679')
    B = ('8214808651328230664709384' +
         '4609550582231725359408128' +
         '4811174502841027019385211' +
         '0555964462294895493038196')
    total = ''
    for n in range(0, 18):
        wanted = (127+19*n)*7**n
        if a_or_b(n) == 'A':
            real = A
        else:
            real = B
        total = real[wanted % 100 - 1] + total

    print(total)


if __name__ == '__main__':
    main()
