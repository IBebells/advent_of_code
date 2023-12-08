
n_bag_cubes = [14, 13, 12] # blue, green, red


def possible_games(puzzle_input: str,n_bag_cubes: list) -> int:

    sum_id = 0
    list_puzzle_input = puzzle_input.split('\n')

    for line in list_puzzle_input:

        possible = True

        game = line.split(' ')

        for element in range(len(game)):

            if 'blue' in game[element]:
                n_blue_cubes = int(game[element - 1])
                if n_blue_cubes > n_bag_cubes[0]:
                    possible = False
                    break

            if 'green' in game[element]:
                n_green_cubes = int(game[element - 1])
                if n_green_cubes > n_bag_cubes[1]:
                    possible = False
                    break

            if 'red' in game[element]:
                n_red_cubes = int(game[element - 1])
                if n_red_cubes > n_bag_cubes[2]:
                    possible = False
                    break

        if possible:
            id = int(game[1].replace(':', ''))
            sum_id = sum_id + id

    return sum_id

def possible_games_two(puzzle_input: str) -> int:

    sum_power = 0
    list_puzzle_input = puzzle_input.split('\n')

    for line in list_puzzle_input:

        bigger_blue = 0
        bigger_green = 0
        bigger_red = 0

        game = line.split(' ')

        for element in range(len(game)):

            if 'blue' in game[element]:
                n_blue_cubes = int(game[element - 1])
                if n_blue_cubes > bigger_blue:
                    bigger_blue = n_blue_cubes

            if 'green' in game[element]:
                n_green_cubes = int(game[element - 1])
                if n_green_cubes > bigger_green:
                    bigger_green = n_green_cubes

            if 'red' in game[element]:
                n_red_cubes = int(game[element - 1])
                if n_red_cubes > bigger_red:
                    bigger_red = n_red_cubes

        power = bigger_blue * bigger_green * bigger_red
        sum_power = sum_power + power

    return sum_power