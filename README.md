
DSP Tools
=========

Created in order for me (Isaac Goss) to learn,
play with, and apply mathematics and techniques of DSP.
Knowledge and algorithms are based upon my reading of SEG [1].

Organization of Features
------------------------

- Superposition / Synthesis / Decomposition Types
    - Constant SUPERPOSITIONS (frozenset of str)
        - impulse
        - forier
        - step
        - even_odd
        - interlaced
- Types
    - signal
        - Scaling a signal by a scalar __mult__ = map(lambda x: x*scalar,...)
        - DC offset __add__ = map(lambda x x+scalar,...)
        - decomposition(str) -> signal, signal
        - synthesis(str, signal) -> signal
- Algorithms
    - superposition


Python Implementation
---------------------

Python 3 implementation is available in the `python` subdirectory.


References
----------

1. (SEG) Smith, Steven W, (1997) _The Scientists and Engineers Guide to Digital Signal Processing_
