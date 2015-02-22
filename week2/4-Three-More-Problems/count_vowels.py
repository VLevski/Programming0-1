text = input("Enter a text: ")

vocal = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

counter = 0

for ch in text:
    if ch in vocal:
        counter += 1

print(text, "-", counter)
