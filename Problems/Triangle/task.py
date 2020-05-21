height = int(input())
for line in range(1, height + 1):
    line_chars = ''
    for char in range(1, (line * 2)):
        line_chars += '#'
    print(line_chars.center(height * 2))
