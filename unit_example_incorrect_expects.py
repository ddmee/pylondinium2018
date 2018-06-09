"""Built-in Assertion error is not so good.
That's why we have assertion helpers in unittest right?

Like self.AssertEqual() method from TestCase class in unittest.

Well, advantage of staying light and nimble with our tooling is I can
user a specific library to deal with improving expectations.

Try a specific library for that."""
# third party
from expects import * # this is normal for usage of expects...
# local lib
from ss_testing import run_tests


# trivally INCORRECT program
def add(a, b):
    return a - b

## Here are my simple tests...
def test_example_1():
    expect(add(1, 2)).to(equal(3))

# THIS TEST WILL PASS BECAUSE 0 - 0 IS THE SAME AS 0 + 0
def test_example_2():
    expect(add(0, 0)).to(equal(0))


if __name__ == '__main__':
    run_tests(tests=[test_example_1, test_example_2])
