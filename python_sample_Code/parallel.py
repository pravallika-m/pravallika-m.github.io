import threading

# write a function to take a number as input and print hello and the number
def print_hello(num):
    print("hello", num)

# write a function to call the above function parallely for 10 times
def parallel_function():
    for i in range(10):
        t = threading.Thread(target=print_hello, args=(i,))
        t.start()

# invoke the above function
parallel_function()


# write unit test for the above program
import unittest
from unittest.mock import patch
from parallel import print_hello

class TestParallel(unittest.TestCase):
    def test_print_hello(self):
        with patch('parallel.print_hello') as mocked_hello:
            print_hello(1)
            mocked_hello.assert_called_with(1)

