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

