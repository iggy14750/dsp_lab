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

def impulse(sig):
    """Decompose an N sample signal into N component signals
    Said signals mean that a system can be analyzed one sample at a time.
    This approach is called convolution (SEG p. 100).

    >>> s = signal([1,2,3])
    >>> decomp = impulse(s)
    >>> decomp
    [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

    >>> decomp[0] + decomp[1] + decomp[2]
    [1, 2, 3]

    >>> sum(decomp)
    [1, 2, 3]
    """
    N = len(sig)
    output_sigs = []
    for n in range(len(sig)):
        output_sigs.append(signal([0]*N))
        output_sigs[n][n] = sig[n]
    return output_sigs

if __name__ == "__main__":
    import doctest
    doctest.testmod()

