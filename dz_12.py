import string
input_srt = input(" Введіть рядок: ")

words = input_srt.split()

hashtag = "#"
for word in words:
    word = ''.join(char for char in word if char not in string.punctuation)

    hashtag += word.capitalize()
hashtag = hashtag [:140]

print(hashtag)
