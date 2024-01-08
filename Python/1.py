# def count_word_occurrences(sentence):
#     words = sentence.split()

#     word_count = {}

#     for word in words:
#         cleaned_word = word.strip('.,!?').lower()

#         word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

#     return word_count

# input = input("Enter a sentence: ")

# word_occurrences = count_word_occurrences(input_sentence)
# for word, count in word_occurrences.items():
#     print(f"{word}: {count}")



def get_first_and_last_two_chars(input_string):
    # Check if the string length is less than 2
    if len(input_string) < 2:
        return "Invalid input: String length is less than 2"
    
    # Extract the first two and last two characters
    result_string = input_string[:2] + input_string[-2:]
    
    return result_string

# Example usage:
input_str = "python"
result = get_first_and_last_two_chars(input_str)

print(result)
