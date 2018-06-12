from ss_testing import run_tests

def keep_it_simple(time_complexity):
    choose_your_tool(time_complexity)

def choose_your_tool(afternoon):
    if afternoon > 1:
        raise AssertionError("Time is greater than one afternoon")

def what_about_python_learning_python():
    time_to_learn = 1000
    keep_it_simple(time_to_learn)

if __name__ == '__main__':
    run_tests([what_about_python_learning_python])

