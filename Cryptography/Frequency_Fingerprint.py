import matplotlib.pyplot as plt

f = open("Catching_Fire.txt", mode='r', encoding='utf-8')
text = f.read()
filtered_text = ""

for character in text:
    if character.isalpha():
        filtered_text += character.lower()
f.close()

letter_frequency = {}

for letter in filtered_text:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

# print(letter_frequency)
letter_list = list(letter_frequency.keys())
freq_list = list(letter_frequency.values())
# print(letter_list, freq_list)

plt.bar(letter_list, freq_list)
plt.ylabel("No. of occurence of letters")
plt.title("Frequency distribution of letters in the Book Catching Fire: The Hunger Games")
plt.show()
