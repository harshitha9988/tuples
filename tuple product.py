def multiply_tuple(numbers: tuple) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product

num_tuple = (2, 3, 4, 5)
result = multiply_tuple(num_tuple)
print(f"The product of the tuple {num_tuple} is {result}")