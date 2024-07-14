import random

def successors_generator(reader):
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

    return successor_map

def generate_text(successor_map, word, length):
    for i in range(length):
        print(word, end=" ")
        successors = successor_map[word]
        next_word = random.choice(successors)
        word = next_word

if __name__ == "__main__":
    reader = open('data/orwell.txt')
    random.seed(2)
    successor_map = successors_generator(reader)

    while True:
        try:
            words = input("Type anything (only one word will be used for context window): ")
            if len(words.split()) > 1:
                raise ValueError("Please enter only one word.")
            word = words.strip('.,;-"'":?-'!()_{}[]").lower()

            length = int(input("How long do you want your text to be: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer!")

            generate_text(successor_map, word, length)
            break   # Exit code if input is valid.
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.")
        except KeyError as e:
            print(f"Word '{word}' not found in the text. Please try another word.")
