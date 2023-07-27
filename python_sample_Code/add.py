
# write a function to add two numbers and return the sum
def add_two_numbers(a, b):
    return a + b

# write unit test cases for the above function
def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 6
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(-1, -1) == -2
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(0, 1) == 1
    assert add_two_numbers(1, 0) == 1

# write a function to subtract two numbers and return the difference
def subtract_two_numbers(a, b):
    return a - b



# invoke the test function to run the test cases
test_add_two_numbers()
