text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, " \
       "facilisis vitae semper at, dignissim vitae libero"

my_list = text.split()
final_list = []
add_cancel = "ing"

for word in my_list:
    if word[-1] in [",", "."]:
        final_list.append(word[:-1] + add_cancel + word[-1:])
    else:
        final_list.append(word + add_cancel)

print(text)
print(" ".join(final_list))
