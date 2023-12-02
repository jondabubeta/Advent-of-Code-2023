def is_game_possible(game):
    # Initialize max values
    max_red = 0
    max_green = 0
    max_blue = 0

    # Loop through all colors and check each values for max
    for cube_set in game:
        colors = cube_set.split(',')
        for color_count in colors:
            count, color = color_count.strip().split()
            count = int(count)
            if color == 'red':
                max_red = max(max_red, count)
            elif color == 'green':
                max_green = max(max_green, count)
            elif color == 'blue':
                max_blue = max(max_blue, count)

    print("RED: ", max_red, "GREEN: ", max_green, "BLUE: ", max_blue, "Product: ", max_red * max_green * max_blue)

    return max_red * max_green * max_blue


def check_games():
    with open('input.txt', 'r') as file:
        games = [line.strip() for line in file]

    minimum = 0

    for game in games:
        game_id, game_data = game.split(': ')
        sets = game_data.split(';')
        product = is_game_possible(sets)
        minimum += product

    print("Minimum Cubes:", minimum)


check_games()
