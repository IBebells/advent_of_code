from functions_day1 import *
from colect_data_module import *
from selenium import webdriver

# firefox webdriver
driver = webdriver.Firefox()

# Autentication
sing_in_github(driver)

# Colete_data
puzzle_input = colet_puzzle_input(driver)

# Sum calibration values (result)
# Parte I
calibration_values_part1 = extract_calibration_values(puzzle_input)

print(sum_calibration_values(calibration_values_part1))

# Parte II
calibration_values_part2 = word_to_numbers(puzzle_input)

print(sum_calibration_values(calibration_values_part2))