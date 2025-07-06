def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_characters(char_counts: dict) -> list:
    char_list = [{"char": c, "num": n} for c, n in char_counts.items() if c.isalpha()]

    def sort_on(item):
        return item["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list