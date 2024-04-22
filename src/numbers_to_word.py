def number_to_french_words(n):

    """Converts a number to its French word representation.

    Args:
        n: An integer.

    Returns:
        The French word representation of the number.
    """


    units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",
             "onze", "douze", "treize", "quatorze", "quinze", "seize"]
    tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]
    exceptions = {71: "soixante-et-onze", 72: "soixante-douze", 73: "soixante-treize", 74: "soixante-quatorze",
                  75: "soixante-quinze", 76: "soixante-seize", 77: "soixante-dix-sept", 78: "soixante-dix-huit",
                  79: "soixante-dix-neuf", 81: "quatre-vingt-un", 82: "quatre-vingt-deux", 83: "quatre-vingt-trois",
                  84: "quatre-vingt-quatre", 85: "quatre-vingt-cinq", 86: "quatre-vingt-six", 87: "quatre-vingt-sept",
                  88: "quatre-vingt-huit", 89: "quatre-vingt-neuf", 91: "quatre-vingt-onze", 92: "quatre-vingt-douze",
                  93: "quatre-vingt-treize", 94: "quatre-vingt-quatorze", 95: "quatre-vingt-quinze",
                  96: "quatre-vingt-seize", 97: "quatre-vingt-dix-sept", 98: "quatre-vingt-dix-huit",
                  99: "quatre-vingt-dix-neuf"}


    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n<0:
        raise TypeError("Input must be a positive integer")


    if n < 0:
        return "négatif " + number_to_french_words(abs(n))

    if n < 17:
        return units[n]
    elif n <= 70:
        if n % 10 == 1:
            return tens[n // 10] + "-et-" + units[n % 10]
        elif n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + "-" + units[n % 10]

    elif n < 100:
        if n in exceptions:
            return exceptions[n]
        elif n % 10 == 0:
            return "quatre-vingt"


    elif n < 1000:
        if n % 100 == 0:
            word=units[n // 100] + "-cents"
            word=word.replace('un-cents','cent')

            return word
        else:
            word=units[n // 100] + "-cent-" + number_to_french_words(n % 100)
            word=word.replace('un-cent','cent')
            return word

    elif n < 1000000:
        if n % 1000 == 0:
            word= number_to_french_words(n // 1000) + "-milles"
            word=word.replace('un-milles','mille')

            return  word
        else:
            word= number_to_french_words(n // 1000) + "-mille-" + number_to_french_words(n % 1000)
            word=word.replace('un-mille','mille')
            return word
    else:
        return "Number out of range, maximum range is 999999"


def main(input_data):
    if isinstance(input_data, list):
        return [(num,number_to_french_words(num)) for num in input_data]
    else:
        return [(input_data,number_to_french_words(input_data))]


if __name__ == "__main__":

    input_data =[45,50,600,7558,99875]

    french_words = main(input_data)
    print("French word representations:")
    for num,word in french_words:
        print( num, ":" , word)
