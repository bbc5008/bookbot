def main():
        path = "books/frankenstein.txt"
        text = get_text(path)
        #word_list = text.split()
        #print(count_words(word_list))
        char_stat_list = characters_dict_to_sorted_list(count_characters(text))
        print("character counts for text")
        for char_stat in char_stat_list:
            print(f"Character {char_stat["Character"]} has {char_stat["Count"]} occurrences")


def get_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(word_list):
    word_counts = {}
    for word in word_list:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_characters(text):
    character_counts = {}
    text = text.lower()
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(dict):
    return dict["Count"]

def characters_dict_to_sorted_list(char_dictionary):
    sorted_char_list = []
    for char in char_dictionary:
        if char.isalpha():
            sorted_char_list.append({"Character" : char, "Count" : char_dictionary[char]})
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list



        


main()