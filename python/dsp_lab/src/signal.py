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
        AssertionError: Provided scalar has type <class 'list'>

        TODO: scalar+signal, signal-scalar, signal+=scalar
        """
        assert type(scalar) in (int, float),\
            "Provided scalar has type " + str(type(scalar))
        return signal(map(lambda sample: sample + scalar, self))

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

        TODO: scalar*signal, signal*=scalar
        """
        assert type(scalar) in (int, float),\
            "Provided scalar has type " + str(type(scalar))
        return signal(map(lambda sample: sample * scalar, self))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

