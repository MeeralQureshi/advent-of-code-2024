import re

def read_input_file():
    file_input = open("day3_input.txt", "r")
    read_file = file_input.read()
    return read_file

def get_multiplied_totals(input):
    multiplied_values = []
    # Find all string matching patterns of 'mul(num1, num2)'
    mul_functions = re.findall("mul\(\d*,\d*\)", input)
    # Multiply num1 and num2 for each mul function and add to multiplied_values array
    for function in mul_functions:
        # Split num1 and num2 from string (around comma)
        num1 = int(function.split(',')[0][4:])
        num2 = int(function.split(',')[1][:-1])
        multiplied_values.append(num1 * num2)
    return multiplied_values

def solve_problem():
    input = read_input_file()
    return get_multiplied_totals(input)

def solve_problem2():
    input = read_input_file()
    # Split input into sections based on 'do()'
    do_functions = re.split("do\(\)", input)
    # Initialize total
    total = 0 
    # For each section, filter out "disabled" sections and sum the rest
    for section in do_functions:
        # Split out sections that have don't - should only be the first entry which is enabled
        exclude_donts = re.split("don't\(\)", section)[0]
        # Split out strings that include 'dont()' from each section
        total += sum(get_multiplied_totals(exclude_donts))
    return total

answer1 = sum(solve_problem())
answer2 = solve_problem2()
print(answer1, answer2)