# Print
-2
print(-2)
print(1, 2, 3)
x = -2
x
print(x)
x = print(-2)
x
print(x)

None
1
'hi'
abs

print(None)
print(1, 2, 3)
print(None, None)
print(print(1), print(2))


def f(x):
    return x + 1

def g(x):
    print(x + 1)

f(3) + 2
# g(3) + 2

# Division
618 / 10
618 // 10
618 % 10
from operator import truediv, floordiv, mod
floordiv(618, 10)
truediv(618, 10)
mod(618, 10)

# Approximation
5 / 3
5 // 3
5 % 3

# Multiple return values
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(618, 10)

# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)

# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x



# Boolean Expressions
True and False

False and False

True and True

True or False

True or True

False or False

1 or True

0 or True

0 or False

False or 0

True and 5 + 2 and 8

True and False and 8

True and False and 8 and 1 and 3

False or print('hi') or True

False or print('hi') or False

True or print('hi') or True

True and print('hi') and True

True and not print('hi') and True

not True

not False

not 0

not 1

not None

not -1

False or True or print('hi')

False or True or 1 / 0

# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
print('i:', i, 'total:', total)