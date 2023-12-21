
def replace_and_reverse(string):

    for symbol in special_symbols:
        string = string.replace(symbol, "@")

    words_list = string.split()
    words_list.reverse()

    return " ".join(words_list)

special_symbols = ["-", ",", ".", "!", "?"]

# We read the text file
with open("text1..txt", "r") as file:
    text = file.readlines()

for line in range(0, len(text), 2):
    sentence = text[line]
    print(replace_and_reverse(sentence))
  
