
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
2. ESP-8266 Hardware Information https://nurdspace.nl/ESP8266
3. ESP-8266 Wiki https://github.com/esp8266/esp8266-wiki/wiki
4. ESP Open SDK https://github.com/pfalcon/esp-open-sdk
5. ESP-8266 Tutorial https://www.instructables.com/How-to-use-the-ESP8266-01-pins/
6. ESP-8266 Wifi Sheild Tutorial https://www.forward.com.au/pfod/CheapWifiShield/ESP2866_01_WiFi_Shield/index.html
7. Using ESP-8266 Tutorial https://www.instructables.com/Using-the-ESP8266-module/
8. ESP-01 Pinout https://cdn.sparkfun.com/datasheets/Wireless/WiFi/ESP8266ModuleV1.pdf
9. ESP-8266 Wikipedia page https://en.wikipedia.org/wiki/ESP8266
10. ESP-8266 Espressif SDK (FreeRTOS) https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/index.html
11. ESP-8266 Datasheet https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf

