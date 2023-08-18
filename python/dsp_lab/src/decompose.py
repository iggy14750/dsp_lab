#!/bin/python3

from signal import signal

def even_odd(sig):
    """Decompose a signal into two using the Even/Odd method.

    For more info, refer to SEG p. 102.

    Each decomposition can be undone using addition.
    >>> sig = signal([1,2,3,4,5])
    >>> even, odd = even_odd(sig)
    >>> even + odd
    [1.0, 2.0, 3.0, 4.0, 5.0]

    The expected values of following the Even/Odd decomposition.
    >>> even
    [3.0, 3.0, 3.0, 3.0, 3.0]
    >>> odd
    [-2.0, -1.0, 0.0, 1.0, 2.0]
    """
    N = len(sig)-1
    even = signal()
    odd = signal()
    for n in range(len(sig)):
        even.append((sig[n] + sig[N-n]) / 2)
        odd.append((sig[n] - sig[N-n]) / 2)
    return (even, odd)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

