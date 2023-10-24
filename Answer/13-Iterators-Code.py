def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]
    >>> next(t)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> d = {'one': 1, 'two': 2, 'three': 3} # Keys and values
    >>> k = iter(d) # next(k)
    >>> v = iter(d.values()) # next(v)
    >>> k = iter(d)
    >>> d.pop('two')
    2
    >>> next(k)
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> r = range(3, 6)
    >>> s = iter(r)
    >>> next(s)
    3
    >>> for x in s:
    ...     print(x)
    4
    5
    >>> for x in s:
    ...     print(x)
    >>> for x in r:
    ...    print(x)
    3
    4
    5
    >>> for x in r:
    ...    print(x)
    3
    4
    5
    """

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def built_in_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t
    False
    >>> list(reversed(t)) == t
    True
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> items = zip(d.keys(), d.values()) # Call next(items)
    """

def plus_minus(x):
    """Yield x and -x.

    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    >>> list(plus_minus(5))
    [5, -5]
    >>> list(map(abs, plus_minus(7)))
    [7, 7]
    """
    yield x
    yield -x

def evens(start, end):
    """A generator function that returns even numbers.

    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

class Countdown:
    """Count down to zero.

    >>> list(Countdown(5))
    [5, 4, 3, 2, 1]
    >>> for x in Countdown(3):
    ...     print(x)
    3
    2
    1
    """
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1
    
def a_then_b_for(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b_for([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a, b):
    """The elements of a followed by those of b.

    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    yield from a
    yield from b

def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k-1)

def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
    

def ones():
    while True:
        yield 1

def nats():
    current = 0
    while True:
        yield current
        current = current + 1

def nats():
    yield 1
    natsStm = nats()
    while True:
        yield 1 + next(natsStm)

def printN(stm, n):
    for _ in range(n):
        print(next(stm))

def notThree():
    yield 1
    yield 2
    notThreeStm = notThree()
    while True:
        yield 3 + next(notThreeStm)

fib_list = []
def fib_iter(n):
    for i in range(n+1):
        if i < 2:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return iter(fib_list)




def fib_gen(n):
    prev = 0
    curr = 1
    for i in range(n):
        if i < 2:
            yield i
            return i
        else:
            newvalue = prev + curr
            prev = curr
            curr = newvalue
            yield curr
            return curr


def fibs():
    yield 0
    yield 1
    fibs1 = fibs()
    fibs2 = fibs()
    next(fibs1)
    while True:
        yield next(fibs1) + next(fibs2)


def f():
    try:
        pass
        def g():
            raise Exception("some error")
    except Exception:
        print("inside f")
    # finally:
    #    print("leaving f")

    return g

def h():
    try:
        f()()
        print("cannot reach here")
    except Exception as e:
        print("inside h, cannot handle it")
        raise e
        print("inside h, cannot reach here")
    finally:
        print("finally here")

h()

s = [1, 2, 3, 4, 5]
for i in s:
    print(i)
    y = s.pop()
    print(s)

i = iter(s)
next(i)
s.pop()
next(i)

