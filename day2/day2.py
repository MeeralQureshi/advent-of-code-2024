import numpy as np

def read_input_file():
    file_input = open("day2_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

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
        # Calculate differences between levels using numpy diff
        differences = np.diff(levels)
        # If all are greater than 1 and less than 3, increment safety
        if all(differences >= 1) and all(differences <= 3):
            safety += 1
        # If all differences are less than -1 and greater than -3, increment safety
        elif all(differences <= -1) and all(differences >= -3):
            safety += 1
    return safety

def solve_problem2():
    # WIP
    pass

answer = solve_problem()
print(answer)