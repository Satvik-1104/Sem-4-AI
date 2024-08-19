from collections import Counter
import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def count_spaces(text):
    spaces = text.count(' ')
    return spaces

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def word_frequencies(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def longest_word(text):
    words = text.split()
    return max(words, key=len)

def average_word_length(text):
    words = text.split()
    total_length = sum(len(word) for word in words)
    num_words = len(words)
    return total_length / num_words if num_words > 0 else 0

if __name__ == "__main__":
    file_path = "2201221_text.txt"
    file_content = read_text_file(file_path)
    if file_content:
        print(f"Number of words: {count_words(file_content)}")
        print(f"Number of lines: {count_lines(file_content)}")
        print(f"Number of spaces: {count_spaces(file_content)}")
        print(f"Number of unique words: {count_unique_words(file_content)}")
        print("Word frequencies:")
        for word, freq in word_frequencies(file_content).items():
            print(f"{word}: {freq}")
        print(f"Longest word: {longest_word(file_content)}")
        print(f"Average word length: {average_word_length(file_content):.2f}")


text_1 = input("Enter text1: ")
print(text_1)
text_2 = input("Enter text2: ")
print(text_2)

if text_1 == text_2:
    print("They are similar: 1")
else:
    print("They are different: 0")