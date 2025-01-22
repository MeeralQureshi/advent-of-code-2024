import numpy as np

def read_input_file():
    file_input = open("day2_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def check_is_safe_report(levels):
    # Calculate differences between levels using numpy diff
    differences = np.diff(levels)
    # All differences are greater than 1 and less than 3
    all_incrementing_in_order = all(differences >= 1) and all(differences <= 3) and levels == sorted(levels)
    # All differences are less than -1 and greater than -3 
    all_decrementing_in_order = all(differences <= -1) and all(differences >= -3) and levels == sorted(levels)[::-1]
    # Return as safe if either of the conditions are met
    return all_incrementing_in_order or all_decrementing_in_order

def check_is_safe_report_with_one_bad_level(levels):
    is_safe_report = check_is_safe_report(levels)
    # If not safe, check if removing one level makes it safe
    if not is_safe_report:
        for i in range(len(levels)):
            # Remove one level
            levels_copy = levels.copy()
            levels_copy.pop(i)
            # Check if safe
            if check_is_safe_report(levels_copy):
                return True
    return is_safe_report

def solve_problem():
    input = read_input_file()
    # Initialize safety score
    safety = 0
    # Loop over each report in input
    for report in input:
        # Split each line
        levels = report.split()
        # Make all levels ints
        levels = [int(level) for level in levels]
        if check_is_safe_report(levels):
            safety += 1
    return safety

def solve_problem2():
    input = read_input_file()
    # Initialize safety score
    safety = 0
    # Loop over each report in input
    for report in input:
        # Split each line
        levels = report.split()
        # Make all levels ints
        levels = [int(level) for level in levels]
        # Check safe scenarios or those with one bad level
        if check_is_safe_report_with_one_bad_level(levels):
            safety += 1            
    return safety

answer1 = solve_problem()
answer2 = solve_problem2()
print(answer1, answer2)