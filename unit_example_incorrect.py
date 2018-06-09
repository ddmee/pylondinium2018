""" Trivally easy to know if implementation is correct... """
# local lib
from ss_testing import run_tests

# trivally INCORRECT program
def add(a, b):
    return a - b

## Here are my simple tests...
def test_example_1():
    assert add(1, 2) == 3

def test_example_2():
    assert add(0, 0) == 0


if __name__ == '__main__':
    run_tests(tests=[test_example_1, test_example_2])
