def sort_on(items):
    return items["num"]

def get_words(text):
    return len(text.split())

def get_chars(text):
    char_dict = {}
    lower = text.lower()
    for char in lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_chars(chars):
    sort_list = []
    for char in chars:
        sort_list.append({"char": char, "num": chars[char]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
