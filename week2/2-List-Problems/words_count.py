user_word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)

start = 1
words = []

while start <= n:
    word = input()
    words += [word]
    start += 1

word_count = 0

for word in words:
    if word == user_word:
        word_count += 1

print(user_word, "is found {} times.".format(word_count))
