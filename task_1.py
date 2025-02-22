def string_to_dict(input_string: str) -> dict:
    """
    This function takes a string and returns a dictionary
    where words are keys and their lengths are values.
    """
    result = {}  # Should be a dictionary instead of a list
    punctuation = ".!?,:/"

    words = input_string.split()

    for word in words:
        word = word.translate(str.maketrans("", "", punctuation))
        result[word] = len(word)

    return result


if __name__ == "__main__":
    user_input_string = input("Please enter a sentence: ")
    dict_value = string_to_dict(user_input_string)
    print("Result:", dict_value)
