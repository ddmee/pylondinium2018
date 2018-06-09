"""
Donal's Stupidly Simply test framework. (ss_testing)

author: mee.donal@gmail.com

Pure python. No weirdness. No compatibility with other test runners.

"""
# standard lib
from typing import Callable, List, Tuple, Union
from traceback import print_exc


def run_tests(tests: List[Callable]) -> bool:
    """Invoke to run all tests in a module.

    :param tests: a list of test functions to run.

    Returns a bool, True if all tests fail, else False.
    """
    print("Stupid simple TESTING! Going to run {} tests.".format(len(tests)))
    # a list of tuples to hold the results when we execute each test function
    test_results = []
    # call the test funcs one after the other.
    for test_fnc in tests:
        # record whether test result in the list
        pass_or_fail, error = _execute_a_test(test_fnc)
        test_results.append(tuple([test_fnc.__name__, pass_or_fail, error]))
    # then pass all results to the end of testing func
    return _end_of_testing(test_results)

def _execute_a_test(test_fnc: Callable) -> Tuple[bool, Union[Exception, None]]:
    """Run a single test method.

    Returns a tuple. First item is a bool of whether test passed or failed.
    Second item is the exception object if test failed, else none..
    """
    pass_or_fail = None
    test_error = None
    try:
        test_fnc()
    #pylint: disable=broad-except
    except Exception as _error:
        print("\n------\nTest failed {}\n".format(test_fnc.__name__))
        print_exc()
        print("\n------\n")
        pass_or_fail = False
        test_error = _error
    else:
        _test_passed()
        pass_or_fail = True
    return pass_or_fail, test_error

def _test_passed() -> None:
    print(".", end="")

def _end_of_testing(test_results: List[Tuple]) -> bool:
    """Prints summary of testing, returns a bool whether all tests passed."""
    print("\nTesting complete. Summary:")
    fail_count = 0
    pass_count = 0
    for result_tuple in test_results:
        if result_tuple[1] is True:
            print("\tTest '{}', passed".format(result_tuple[0]))
            pass_count += 1
        else: # presume to have failed
            print("\tTest '{}', failed.".format(result_tuple[0]))
            fail_count += 1
    print("Total passed: {}. Total failed {}.".format(pass_count, fail_count))

    # if fail count is 0, bool is False. That's actually indication all
    # tests passed. If fail count is anything other than 0, return False.
    return not bool(fail_count)
