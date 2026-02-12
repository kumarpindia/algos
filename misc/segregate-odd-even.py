# This function takes a list of integers and rearranges it so that all even numbers come before all odd numbers.
# The relative order of the even and odd numbers does not matter.

# For example, given the input [5, 8, 1, 3, 7, 9, 2], a valid output would be [8, 2, 1, 3, 7, 9, 5] (or any
# other order of evens followed by odds).
# The function should return the rearranged list.
# Note: The function should modify the input list in place and return it.
# For example, given the input [1, 2, 3, 4], a valid output would be [2, 4, 1, 3] (or any other order of evens
# followed by odds).

def segregate_evens_and_odds(numbers):
    
    last_even_index = 0

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            if i != last_even_index:
                numbers[last_even_index], numbers[i] = numbers[i], numbers[last_even_index]
            last_even_index += 1
    
    return numbers


print(segregate_evens_and_odds([5, 8, 1, 3, 7, 9, 2])) # Output: [8, 2, 1, 3, 7, 9, 5] (or any other order of evens followed by odds)
print(segregate_evens_and_odds([1, 2, 3, 4])) # Output: [2, 4, 3, 1] (or any other order of evens followed by odds)
print(segregate_evens_and_odds([4, 9, 5, 2, 9, 5, 7, 10])) # Output: [4, 2, 10, 9, 9, 5, 7, 5] (or any other order of evens followed by odds)
print(segregate_evens_and_odds([5, 8, 3, 9, 4, 1, 7])) # Output: [8, 4, 3, 9, 5, 1, 7] (or any other order of evens followed by odds)
print(segregate_evens_and_odds([4, 7, 8])) # Output: [4, 8, 7] (or any other order of evens followed by odds)