def alphabet_position(text):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    ListedText = list(text)
    for i in ListedText:
        for j in alphabets:
            if str(j) == str(i):
                i_index = ListedText.index(i)
                ListedText[i_index] = str(alphabets.index(j) + 1)
    text = "".join(ListedText)
    return text
print(alphabet_position("@mandliwh2"))
