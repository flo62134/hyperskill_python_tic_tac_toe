text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

max_length = int(input())
max_length_words = [word for sentence in text for word in sentence if len(word) <= max_length]
print(max_length_words)
