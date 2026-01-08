# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    row = 1
    column = 1

    while row <= 1 or row <= n:
        result += ("*" * n)

    while 1 < row < n:
        result += "*   *"
        
    return result.rstrip()
print(hollow_square(5))


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(1, n + 1): 
        for j in range(1, i + 1):
            # print(, end="")
            result += str(j)
        #print()
        result += "\n"

    return result.rstrip()

print(number_pattern(4))
        
#     pattern = ""
#     for i in range(1, n + 1):
#         line = ""
#         for number in range(1, i + 1):
#             line += str(number)
#         pattern += line + "\n"
#     return pattern
# print(pattern)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    i = 1
    count = 1
    total = 0

    while i <= n:
        total += count
        i += 1
        count += 1

    return total
print(sum_of_natural_numbers(5))


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):

        for j in range(n - i - 1):
            result += " "
    
        for k in range(2 * i + 1):
            result += "*"
        
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))
