# Decorators
Used to dynamically alter the functionality of your functions.
For example, if you want to have the option to time any specific function,
you can call that function with the decorator which will return your function
with the additional functionality of timing the original function.

the wrapper is the part that adds this functionality and the outer function returns the wrapper (which is just the original function + added functionality)