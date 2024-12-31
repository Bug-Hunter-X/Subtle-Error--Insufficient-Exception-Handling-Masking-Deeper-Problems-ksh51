def function_with_improved_error_handling(data):
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")

    if 'key' not in data:
        raise KeyError("The key 'key' is missing from the input data")

    try:
        result = data['key']
        return result
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}") from e

# Example of how the function might be used:
my_data = {'key': 10}
result = function_with_improved_error_handling(my_data)
print(f"Result: {result}")

my_data = {}
#This will raise a KeyError
try:
    result = function_with_improved_error_handling(my_data)
    print(f"Result: {result}")
except KeyError as e:
    print(f"Caught specific exception: {e}")

my_data = [1, 2, 3]  #This will raise a ValueError
try:
    result = function_with_improved_error_handling(my_data)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Caught specific exception: {e}")
