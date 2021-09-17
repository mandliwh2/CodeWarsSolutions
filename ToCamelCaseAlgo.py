def to_camel_case(text):
    textListed = list(text)
    for i in textListed:
        index = textListed.index(i)
        if i == "-" or i == "_":
            textListed[index] = ""
            UpperCar = textListed[index + 1].upper()
            textListed[index + 1] = UpperCar
    text = "".join(textListed)
    print(text)
to_camel_case("the-warrior_gp")

