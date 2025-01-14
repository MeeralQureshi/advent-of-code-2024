from collections import defaultdict

def read_input_file():
    file_input = open("day1_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file()
    # Initialize 3 lists, 2 for the numbers and one for the differences
    first_ids = []
    second_ids = []
    differences = []
    # Read one line at a time
    for line in input:
        # Split the line into the two numbers
        numbers = line.split()
        # Add the first number to the first list
        first_ids.append(int(numbers[0]))
        # Add the second number to the second list
        second_ids.append(int(numbers[1]))
    # Sort both lists into ascending order
    first_ids.sort()
    second_ids.sort()
    # Go through both lists and populate the third with the difference
    for i in range(len(first_ids)):
        differences.append(abs(second_ids[i] - first_ids[i]))
    # Sum all the differences to get the total distance
    total_distance = sum(differences)
    # Return the total distance
    return total_distance

def solve_problem2():
    input = read_input_file()
    # Initialize 2 lists for the numbers
    first_ids = []
    second_ids = []
    # Read one line at a time
    for line in input:
        # Split the line into the two numbers
        numbers = line.split()
        # Add the first number to the first list
        first_ids.append(int(numbers[0]))
        # Add the second number to the second list
        second_ids.append(int(numbers[1]))
    # Initialize a dictionary to keep track of how many times each number in first list appears in second list
    number_count = defaultdict(int)
    # Go through the first list
    for number in first_ids:
        for number2 in second_ids:
            # For each number, add dictionary entry with the number as the key and the number of times it appears in the second list as the value
            if number == number2:
                number_count[number] += 1
    # Sum all the values in the dictionary to get the similarity score
    similarity_score = sum(key * value for key, value in number_count.items())
    # Return the similarity score
    return similarity_score

answer = solve_problem2()
print(answer)