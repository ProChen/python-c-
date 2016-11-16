#!/usr/bin/python
from ctypes import cdll
libtest = cdll.LoadLibrary("./libtest.so")
libtest.test_a()
libtest.test_b()

