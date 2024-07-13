import random

reader = open('data/orwell.txt')
successor_map = {}
context_window = []

for line in reader:
    for word in line.split():
        cleaned_word = word.strip('.,;-"'":?-'!()_{}[]").lower()
        context_window.append(cleaned_word)

        if len(context_window) == 2:
            key = context_window[0]
            value = context_window[1]
            if key in successor_map:
                successor_map[key].append(value)
            else:
                successor_map[key] = [value]
            context_window.pop(0)

print(successor_map['and'])
