def num_words(total_words):
    string_of_words = total_words.split()
    number_of_words = 0
    for word in string_of_words:
        number_of_words +=1
    return number_of_words

def num_character(total_words):
    lower_case = total_words.lower()
    character_dict={}
    for i in lower_case:
        if i in character_dict:
            character_dict[i] += 1
        else:
            character_dict[i] = 1
    return character_dict

def sorted_dict(num_character):
    list_of_dicts = []
    for i in num_character:
        dict1 = {"char" : i, "num" : num_character[i]}
        list_of_dicts.append(dict1)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(num_character):
    return num_character["num"]
