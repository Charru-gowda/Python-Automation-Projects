import re

def count_me():
    freq = {}  # To store the word and its corresponding word count

    # Open the file safely using 'with'
    with open('count.txt', 'r') as file_obj:
        word_content = file_obj.read().lower()  # Convert all words to lowercase

    # Find all words of length 3–15
    reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)

    # Count frequency
    for word in reg_exp:
        freq[word] = freq.get(word, 0) + 1

    # Print results
    for word, count in freq.items():
        print(word, count)


if __name__ == '__main__':
    count_me()
