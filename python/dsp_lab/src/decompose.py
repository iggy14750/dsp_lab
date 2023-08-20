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

def step(sig):
    """Decompose an N sample signal into N component signals
    Each of which begins with a run of 0s, followed by a "step" to a different value, at which point is plateas.

    >>> s = [5,2,9]
    >>> x = step(s)
    >>> x
    [[5, 5, 5], [0, -3, -3], [0, 0, 7]]

    >>> sum(x)
    [5, 2, 9]
    """
    N = len(sig)
    output_sigs = []
    # Special case for x_0[n]
    output_sigs.append(signal([sig[0]]*N))
    for n in range(1, N):
        this_sig = []
        step_val = sig[n] - sig[n-1]
        this_sig += [0] * n
        this_sig += [step_val] * (N - n)
        output_sigs.append(signal(this_sig))
    return output_sigs

def interlaced(sig):
    """Interlaced decomposition simply breaks a signal into two components.
    One of which deals with each sample at an even offset / index.
    And the other deals with the signals at odd offsets / indecies.

    >>> s = signal([8, 6, 7, 5, 3, 0, 9])
    >>> even, odd = interlaced(s)
    >>> even
    [8, 0, 7, 0, 3, 0, 9]
    >>> odd
    [0, 6, 0, 5, 0, 0, 0]
    >>> even + odd
    [8, 6, 7, 5, 3, 0, 9]
    """
    even = signal()
    odd = signal()
    for i in range(len(sig)):
        even.append(0)
        odd.append(0)
        if i % 2 == 0:
            even[i] = sig[i]
        else:
            odd[i] = sig[i]
    return (even, odd)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

