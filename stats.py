def get_word_count(file_path):
    words = file_path.split()
    return len(words)

def get_letters(file_path):
    letter_counts = {}
    for char in file_path:
        char = char.lower()
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1            
    return letter_counts

def sort_dictionary(file_path):
    def sort_on(file_path):
        return file_path["num"]
    
    print(get_letters(file_path).sort(reverse=True, key=sort_on))