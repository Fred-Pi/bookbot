def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
