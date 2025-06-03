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

# This function takes a character count dictionary and returns a sorted list
def sort_characters(char_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Sort by count (num) in descending order (greatest to least)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list