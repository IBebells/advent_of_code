from functions_day2 import *
from colect_data_module import *
from selenium import webdriver

n_bag_cubes = [14, 13, 12] # blue, green, red

# firefox webdriver
driver = webdriver.Firefox()

# Autentication
sing_in_github(driver)

# Colete_data
puzzle_input = colet_puzzle_input(driver, 'https://adventofcode.com/2023/day/2/input')

# Sum IDs
print(possible_games(puzzle_input, n_bag_cubes))

# Sum Power
print(possible_games_two(puzzle_input))

