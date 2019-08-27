# Python-beginners-tasks
def longest_word(words):
    word_len = []
    for x in words:
        word_len.append((len(x), x))
    word_len.sort()
    return word_len[-1][1]
print(longest_word(["Ashish", "Kumar", "Bhuwaniya"]))
