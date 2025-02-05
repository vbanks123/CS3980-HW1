# fib.py


import functools as ft
from functools import lru_cache
import time
import matplotlib.pyplot as plt


# this timer decorator is used to measure the execution time
def timer(func):
    @ft.wraps(func)
    # wrap accepts named and unnamed arguments
    def wrap(*args, **kwargs):

        # start timing the run time
        start = time.perf_counter()
        # calling the function
        result = func(*args, **kwargs)
        # end the timing
        end = time.perf_counter()
        execution_time = end - start
        print(
            f"Finished in {execution_time:.10f}s: "
            f"{func.__name__}({args if args else ''}) -> {result}"
        )
        # return both the result and the time taken
        return result, execution_time

    # returning the decorated function
    return wrap


# storing the previous runs
@lru_cache(maxsize=None)
# applying the time decorator
@timer
def fib(n: int) -> int:
    # if n is less than 2, return n
    if n < 2:
        return n
    # extracting the results
    return fib(n - 1)[0] + fib(n - 2)[0]


if __name__ == "__main__":
    # computing the fibonacci for n = 1 and continuing until 100
    n_value = list(range(1, 101))
    times = []

    for n in n_value:
        # getting the execution time (_ is a tuple unpacking; we only want the execution time)
        _, ex_time = fib(n)
        times.append(ex_time)

    # plotting the execution times
    # setting size of the figure
    plt.figure(figsize=(10, 5))
    # plotting n and time
    plt.plot(n_value, times, marker="o", linestyle="-")
    plt.xlabel("n in Fibonacci Sequence")
    plt.ylabel("Execution Time (Seconds)")
    plt.title("Execution Time for Fibonacci Computation")
    # adding grid lines to the plot
    plt.grid()
    # showing the plot
    plt.show()
