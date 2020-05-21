lower = input()
words = lower.split()
upper_words = [word.title() for word in words]
upper_words[0] = upper_words[0].lower()
camel = "".join(upper_words)
print(camel)
