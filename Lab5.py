# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    hollow_squares = ["*" * n]
    for hollow_squares in range(n):
        print(hollow_squares)
    for hollow_squares in range(n-3):
        print(hollow_squares)
    return "*" * n


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
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""
