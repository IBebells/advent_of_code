# Functions for day 1

def word_to_numbers(puzzle_input:str) -> list:

    calibration_values = []
    digits = {'one': '1', 'two': '2','three': '3','four': '4', 'five':'5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # transform puzzle_input elements in a list
    puzzle_input_list = puzzle_input.split('\n')
    
    for element in puzzle_input_list:
        front = ''
        behind = ''
        find_front_number = False
        find_behind_number = False
        for caractere in element:
            front = front + caractere
            if not find_front_number:
                for word, number in digits.items():
                    if word in front or number in front:
                        front_number = number
                        find_front_number = True
            else:
                break
                
        element = element[::-1]
        for caractere in element:
            behind = caractere + behind
            if not find_behind_number:
                for word, number in digits.items():
                    if word in behind or number in behind:
                        behind_number = number
                        find_behind_number = True
            else:
                break

        calibration_value = int(front_number + behind_number)
        calibration_values.append(calibration_value)
    
    return calibration_values

def extract_calibration_values(puzzle_input:str) -> list: 

    # transform puzzle_input elements in a list
    puzzle_input_list = puzzle_input.split('\n')

    numbers = []
    calibration_values = []
    numbers_list = [number for number in range(1,10)]

    for element in puzzle_input_list:
        for caractere in element:
            if caractere in str(numbers_list):
                numbers.append(caractere)

        calibration_value = int(numbers[0] + numbers[-1])
        calibration_values.append(calibration_value)
        numbers = []

    return calibration_values

def sum_calibration_values(calibration_values:list) -> int:

    sum = 0


    for calibration_value in calibration_values:
        sum += calibration_value

    return sum