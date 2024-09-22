def filterEvenNumbers(numbers):
    # Use a list comprehension to filter even numbers
    return [num for num in numbers if num % 2 == 0]

# Example usage
print(filterEvenNumbers([1, 2, 3, 4, 5]))        # Output: [2, 4]
print(filterEvenNumbers([10, 15, 20, 25]))       # Output: [10, 20]
print(filterEvenNumbers([7, 11, 13]))             # Output: []
print(filterEvenNumbers([0, -2, -4]))              # Output: [0, -2, -4]