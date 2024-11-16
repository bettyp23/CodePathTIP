# Building a Recursive Function
# Every recursive function has at least two main components:

# The base case End condition. Describes the condition and code that should run when we want our function to stop making recursive calls. Often the base case is the smallest subproblem of the overall problem we are working to solve.
# The recursive case Code to execute in all other cases. The recursive case calls the function again, but usually passes in a smaller or simpler input to move us closer to reaching the base case.
def count_recursive(num):
    # Action to repeat
    print(f"Count {num}!")

    # Base Case: If num is 1 we want to stop counting down
    if num == 1:
        # Terminate the function by returning
        return

    # Recursive Case: If num is larger than 1
    else:
       # Call count_recursive() again, but decrement the input value by 1
       count_recursive(num - 1)
# A recursive function may have multiple base cases. This is useful when we have multiple conditions under which we want to stop repeating our function body and want to specify different behavior for each condition.

# Example Usage:

# Check if a given value is odd
def is_odd(n):

  # Base Case 1: n is 0, which is not odd  
  if n == 0:
    # Return False
    return False
  # Base Case 2: n is 1, which is odd
  if n == 1:
    # Return True
    return True

  # Recursive case: n is greater than 1
  else:
    # Check if the input subtracted by 2 is odd
    # If n - 2 is odd, n must also be odd
    return is_odd(n - 2)

test_odd_value = is_odd(5) 
test_even_value = is_odd(6)

print(test_odd_value) # Prints True
print(test_even_value) # Prints False