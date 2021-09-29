import re
# Input text
texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]


# Parser for each string in an input text
def parsestr(current_row_number, current_text_line):
    list_of_words = re.findall(r'\w+', current_text_line)
    for word in list_of_words:
        word_in_lower = word.lower()
        if word_in_lower in dictionary:
            dict_row_number, dict_word_count = dictionary[word_in_lower]
            dictionary[word_in_lower] = (dict_row_number, dict_word_count+1)
        else:
            dictionary[word_in_lower] = (current_row_number, 1)


# Main code
dictionary = {}
for row_number, text_line in enumerate(texts):
    parsestr(row_number, text_line)

# Print header
print(f"{'word' : <10}{'count' : <10}{'first line' : <10}")

# Print values
for i in dictionary.items():
    result_word, (result_row_number, result_word_count) = i
    print(f"{result_word : <10}{result_word_count : <10}{result_row_number : <10}")
