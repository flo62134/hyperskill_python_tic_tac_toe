# write your code here
def print_border():
    print('---------')


def print_lines(grid_string: str):
    chars = list(grid_string)
    for x in range(0, 3):
        print_line(chars, x)


def print_line(grid_chars, line_number):
    line = ''
    line += '| '
    for y in range(0, 3):
        current_char = grid_chars[(3 * line_number) + y]
        line += f"{current_char} "
    line += '|'
    print(line)


grid = input()
print_border()
print_lines(grid)
print_border()
