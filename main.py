# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max([num1, num2, num3])
print(max_num(3, 6, 10))
print(max_num(13, 6, 10))
print(max_num(3, 16, 10))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(nums):
    result = 1
    for num in nums:
        result *= num
    return result
numbers = [2, 3, 4, 5]
print(mult_list(numbers))

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]
print(rev_string("Hello"))

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, a, b):
    return num in range(a, b + 1)
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    rows = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
        rows.append(row)
    for row in rows:
        print(" ".join(str(num) for num in row))
pascal(1)
pascal(5)