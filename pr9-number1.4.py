from string import punctuation

def search(word):
    vowels = 'aeiouAEIOU'
    return word[0] in vowels

vowels_count = 0
consonant_count = 0
words = []

with open("Stix.txt", "r") as file:
    stix = file.read()
    for word in stix.split():
        cleaned_word = word.strip(punctuation)
        words.append(cleaned_word)

for word in words:
    if search(word):
        vowels_count += 1
    else:
        consonant_count += 1

print(f"Стих:\n{stix}\nКоличество слов начинающихся на гласную букву: {vowels_count}\nКоличество слов начинающихся на согласную: {consonant_count}")
