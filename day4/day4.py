def read_input_file():
    file_input = open("day4_input.txt", "r")
    read_file = file_input.read()
    rows = read_file.split("\n")
    word_search = [[letter for letter in row] for row in rows] 
    return word_search

SEARCH_WORD = "XMAS"
MAS_SEARCH_WORD = "MAS"

# These can be refactored to reduce repeated code, but kept them verbose for readability
def check_up(word_search, row, col):
    if row - 3 >= 0:
        check_word = word_search[row][col] + word_search[row - 1][col] + word_search[row - 2][col] + word_search[row - 3][col]
        return check_word == SEARCH_WORD
    return False

def check_down(word_search, row, col):
    if row + 3 < len(word_search):
        check_word = word_search[row][col] + word_search[row + 1][col] + word_search[row + 2][col] + word_search[row + 3][col]
        return check_word == SEARCH_WORD
    return False

def check_left(word_search, row, col):
    if col - 3 >= 0:
        check_word = word_search[row][col] + word_search[row][col - 1] + word_search[row][col - 2] + word_search[row][col - 3]
        return check_word == SEARCH_WORD
    return False

def check_right(word_search, row, col):
    if col + 3 < len(word_search[row]):
        check_word = word_search[row][col] + word_search[row][col + 1] + word_search[row][col + 2] + word_search[row][col + 3]
        return check_word == SEARCH_WORD
    return False

def check_upleft(word_search, row, col):
    if row - 3 >= 0 and col - 3 >= 0:
        check_word = word_search[row][col] + word_search[row - 1][col - 1] + word_search[row - 2][col - 2] + word_search[row - 3][col - 3]
        return check_word == SEARCH_WORD
    return False

def check_upright(word_search, row, col):
    if row - 3 >= 0 and col + 3 < len(word_search[row]):
        check_word = word_search[row][col] + word_search[row - 1][col + 1] + word_search[row - 2][col + 2] + word_search[row - 3][col + 3]
        return check_word == SEARCH_WORD
    return False

def check_downleft(word_search, row, col):
    if row + 3 < len(word_search) and col - 3 >= 0:
        check_word = word_search[row][col] + word_search[row + 1][col - 1] + word_search[row + 2][col - 2] + word_search[row + 3][col - 3]
        return check_word == SEARCH_WORD
    return False

def check_downright(word_search, row, col):
    if row + 3 < len(word_search) and col + 3 < len(word_search[row]):
        check_word = word_search[row][col] + word_search[row + 1][col + 1] + word_search[row + 2][col + 2] + word_search[row + 3][col + 3]
        return check_word == SEARCH_WORD
    return False

def solve_problem():
    word_search = read_input_file()
    search_counter = 0
    # For each letter in each row, check all possible directions and increment the counter if the word is found
    for row in range(len(word_search)):
        for col in range(len(word_search[row])):
            # Again, these can be refactored to reduce repeated code, but kept them verbose for readability
            if check_up(word_search, row, col):
                search_counter += 1
            if check_down(word_search, row, col):
                search_counter += 1
            if check_left(word_search, row, col):
                search_counter += 1
            if check_right(word_search, row, col):
                search_counter += 1
            if check_upleft(word_search, row, col):
                search_counter += 1
            if check_upright(word_search, row, col):
                search_counter += 1
            if check_downleft(word_search, row, col):
                search_counter += 1
            if check_downright(word_search, row, col):
                search_counter += 1
    return search_counter

def check_left_diagonal(word_search, row, col):
    check_word =  word_search[row - 1][col - 1] + word_search[row][col] + word_search[row + 1][col + 1]
    word_matches = check_word == MAS_SEARCH_WORD or check_word == MAS_SEARCH_WORD[::-1]
    return word_matches

def check_right_diagonal(word_search, row, col):
    check_word = word_search[row + 1][col - 1] + word_search[row][col] + word_search[row - 1][col + 1]
    word_matches = check_word == MAS_SEARCH_WORD or check_word == MAS_SEARCH_WORD[::-1]
    return word_matches

def is_x_shape(word_search, row, col):
    # Check bounds
    if row - 1 >= 0 and row + 1 < len(word_search) and col - 1 >= 0 and col + 1 < len(word_search[row]):
        # If in bound, check diagonals in both directions
        return check_left_diagonal(word_search, row, col) and check_right_diagonal(word_search, row, col)
    return False

# Again, these can be refactored to reduce repeated code, but kept them verbose for readability
def solve_problem2():
    word_search = read_input_file()
    search_counter = 0
    # For each letter in each row, check all possible directions and increment the counter if the word is found
    for row in range(len(word_search)):
        for col in range(len(word_search[row])):
            # Again, these can be refactored to reduce repeated code, but kept them verbose for readability
            if is_x_shape(word_search, row, col):
                search_counter += 1
    return search_counter

answer1 = solve_problem()
answer2 = solve_problem2()
print(answer1, answer2)