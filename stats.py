# This function counts words 
def count_words(text):
    words = text.split()
    return len(words)

# This function counts characters and returns a dictionary
def count_characters(text):
    char_count = {}
    # Convert text to lowercase to avoid duplicates
    text_lower = text.lower()
    
    # Count each character
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count