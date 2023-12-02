def is_game_possible(red_limit, green_limit, blue_limit, game):
    for cube_set in game:
        red_count = 0
        green_count = 0
        blue_count = 0

        colors = cube_set.split(',')
        for color_count in colors:
            count, color = color_count.strip().split()
            count = int(count)
            if color == 'red':
                red_count += count
            elif color == 'green':
                green_count += count
            elif color == 'blue':
                blue_count += count

        print("RED_COUNT:", red_count, "   GREEN_COUNT:", green_count, "   BLUE_COUNT:", blue_count)

        if red_count > red_limit or green_count > green_limit or blue_count > blue_limit:
            return False

    return True


def check_games():
    with open('input.txt', 'r') as file:
        games = [line.strip() for line in file]

    red_limit = 12
    green_limit = 13
    blue_limit = 14

    # Check which games are possible and store the IDs of possible games
    possible_games = []

    for game in games:
        game_id, game_data = game.split(': ')
        sets = game_data.split(';')
        if is_game_possible(red_limit, green_limit, blue_limit, sets):
            # Extract the numeric part of "Game X"
            game_id = int(game_id.split(' ')[1])
            possible_games.append(game_id)

    # Calculate the sum of the IDs of possible games
    sum_games = sum(possible_games)

    # Print the result
    print("Possible Game IDs:", possible_games)
    print("Sum Game IDs:", sum_games)


check_games()
