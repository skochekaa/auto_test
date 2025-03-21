words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    my_word = ""
    for i in range(value):
        my_word += key
    print(my_word)
