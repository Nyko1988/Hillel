# you have fix codestyle (I will check it using flake8), write add typehinting, rename objects if it is necessary
# I will use mypy as well
# you have to fix functions if they work in incorrect way
# write documentation
# remember about namings, especially builtins
# you have to add tests (check errors, types and different values)  and manage its location
# the main idea of this homework - write readable and maintainable code
# function that are called directly here nust be moved to special main file
# it is not a joke - sometimes I receive this kind of code in homeworks
# do not forget about requirements.txt
import lib


str = 2  # this is just a piece of code to refactor and test
print(lib.random_string_generation(20.))
print(lib.random_string_generation(-1))
print(lib.get_random_number())
print(lib.random_string_generation(1.0))
print(lib.random_string_generation())
