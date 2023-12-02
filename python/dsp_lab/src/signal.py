#!/bin/python3

class signal(list):
    """Represents a signal in the DSP sense.
    Extends python list, with only a few method overrides.
    TODO: Could re-implement with numpy arrays for performance.
    Each said override will include it's own test cases.
    First, here, basic list functionality is ensured.

    Note on terminology
    - "signal" refers to either this class, or instances thereof.
      A signal is a list filled with numericl data.
    - "sample" is one datum stored in said list.
      Consider it one measurement in a descreete-time system, ie, sound.
    - "scalar" is a single number which is used in a calculation.

    >>> s = signal([1,2,3])
    >>> s[0]
    1
    >>> s.append(77)
    >>> s[-1]
    77
    >>> len(s)
    4
    >>> s.pop()
    77
    >>> len(s)
    3
    """

    @staticmethod
    def impulse(length=5, position=2, value=1):
        """
        Generate a signal object which can be used to generate an impulse response to a system.
        Said impulse signal is composed of all zeroes, except for one non-zero sample.
        Said non-zero element is the value 1 by default, but can be set this value as well.
        As well as the value, the overall length of the signal, as well as the index / position of that non-zero element within the signal.
        The default impulse if no arguments are given is 

        >>> signal.impulse()
        [0, 0, 1, 0, 0]

        >>> signal.impulse(length=4, position=1, value=3)
        [0, 3, 0, 0]

        >>> signal.impulse(7, 0, 2)
        [2, 0, 0, 0, 0, 0, 0]
        """
        s = signal([0]*length)
        s[position] = value
        return s

    def __add__(self, scalar):
        """Use the + operator to add a DC offset to signal.
        That is, add provided scalar to each sample of the signal.

        Adding an integer scalar to signal will add it to each sample.
        >>> s = signal([1,2,3])
        >>> s + 4
        [5, 6, 7]

        Note that these operations do NOT modify the existing signal object
        >>> s + (-1)
        [0, 1, 2]

        Floats are also supported.
        TODO how to test this with float equality?
        >> s + 3.14
        [4.14, 5.14, 6.14]

        Attempting to add non-scalars will throw.
        >>> s + [4,5,6]
        Traceback (most recent call last):
            ...
        TypeError: Provided scalar has type <class 'list'>

        The positions of signal and scalar can reverse.
        >>> 3 + s
        [4, 5, 6]

        We can also use the subtraction operator.
        >>> s - 1
        [0, 1, 2]

        Modify the signl in place using the += operator.
        >>> s += 2
        >>> s
        [3, 4, 5]

        Attempt to add non-scalar.
        >>> s += {45: 2}
        Traceback (most recent call last):
            ...
        TypeError: Provided scalar has type <class 'dict'>

        Sythesize two signals together, by adding them piece-wise.
        >>> signal([1,2,3]) + signal([6,5,4])
        [7, 7, 7]

        Using said synthesis must return a "signal" as well
        >>> type(signal([1,2,3]) + signal([6,5,4]))
        <class '__main__.signal'>

        Attempting to add two signals of inequal lengths will throw.
        >>> signal([3,4,2]) + signal([3])
        Traceback (most recent call last):
            ...
        TypeError: Provided scalar has type <class '__main__.signal'>

        Synthesize two vectors in-place
        >>> s += signal([6, 1, 2])
        >>> s
        [9, 5, 7]
        
        Override  __repr__ from list?
        TODO: Better Exceptions raised.
        """
        if type(scalar) in (int, float):
            return signal(map(lambda sample: sample + scalar, self))
        elif type(scalar) == signal and len(self) == len(scalar):
            output = signal()
            for i in range(len(self)):
                output.append(self[i] + scalar[i])
            return output
        else:
            raise TypeError("Provided scalar has type " + str(type(scalar)))

    def __radd__(self, scalar):
        return self + scalar
    def __sub__(self, scalar):
        return self + (-1*scalar)
    def __iadd__(self, scalar):
        return self + scalar


    def __mul__(self, scalar):
        """Use the * operator to scale the signal by a scalar.
        That is, multiply each sample of the signal by the scalar.
        This overrides the existing * operator, which crates copies of the list.

        Multiplying an integer scalar by signal will mult it by each sample.
        >>> s = signal([1,2,3])
        >>> s * 4
        [4, 8, 12]

        Note that these operations do NOT modify the existing signal object
        >>> s * (-1)
        [-1, -2, -3]

        Attempting to add non-scalars will throw.
        >>> s * [4,5,6]
        Traceback (most recent call last):
            ...
        AssertionError: Provided scalar has type <class 'list'>

        scalar * signal
        >>> 5 * s
        [5, 10, 15]

        In-place signal *= scalar
        >>> s *= 3
        >>> s
        [3, 6, 9]

        Division by scalar. TODO: Floating-point comparisons.
        In-place division by a scalar.

        How does order of operations work?
        >>> 5 * s + 1
        [16, 31, 46]
        """
        assert type(scalar) in (int, float),\
            "Provided scalar has type " + str(type(scalar))
        return signal(map(lambda sample: sample * scalar, self))
    def __rmul__(self, scalar):
        return self * scalar
    def __imul__(self, scalar):
        return self * scalar
    def __rshift__(self, num):
        """
        Shift this signal to the right-hand direction,
        meaning that the right-most elements of this signal will be
        dropped, while the same number of zeros are
        appended to the left-hand side.
        The signal generated by this operation shall be the same length
        as the input signal on which it was called.

        >>> signal([1,2,3,4,5,6]) >> 2
        [0, 0, 1, 2, 3, 4]
        """
        res = signal([0]*len(self))
        for i in range(0, len(self)-num):
            #res.append(self[i])
            res[i+num] = self[i]
        assert len(res) == len(self)
        return res


    def __xor__(self, other):
        """
        Calculate the convolution of this signal with the given input signal.

        Consider [x,x,x] ^ [y,y,y,y,y]...
        The first argument, x, is shifted across the length of y,
        such that at each step, the following is calculated,
        and then added to an accumulator signal.
        
        [y, y, y, y, y]
            |
            y
               *
        [0, x, x, x, 0]
               =
        [0,xy,xy,xy, 0]

        Given vectors x[N] and y[M],
        the length of x[N] ^ y[M] shall be N+M-1
        >>> x = signal([1,0,0])
        >>> y = signal([1,2,3])
        >>> len(x ^ y)
        5
        >>> x ^ y
        [1, 2, 3, 0, 0]

        >>> x = signal([2,4,7,0])
        >>> y = signal([7,3,1,6,9,2,3,5,2,3])
        >>> x ^ y
        [14, 34, 63, 37, 49, 82, 77, 36, 45, 49, 26, 21, 0]

        >>> x = signal([-3.2, -1.4, 0.3, 2.5])
        >>> y = signal([1.0, 0.75, 0.5, 0.25, 0, -0.25, -0.5, -0.75, -1])
        >>> list(map(lambda elem: round(elem, 4), x ^ y))
        [-3.2, -3.8, -2.35, 1.225, 1.675, 2.125, 2.575, 3.025, 3.475, -0.075, -2.175, -2.5]
        """
        N = len(self)
        M = len(other)
        res = signal.impulse(length=N+M-1, value=0)
        for i, factor in enumerate(other):
            scaled = factor * self
            # Extend the scaled x signal to that of
            # the signal resultant from this function.
            addend = signal([0]*len(res))
            for j in range(len(self)):
                addend[j] = scaled[j]
            res += addend >> i
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()

