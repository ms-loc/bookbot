def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def sort_letters(letter_dict):
    l_array = []
    for l in letter_dict:
        if l.isalpha():
            l_array.append({"letter": l, "num": letter_dict[l]})
            
    def sort_on(dict):
        return dict["num"]
            
    l_array.sort(reverse=True, key=sort_on)
    
    return l_array