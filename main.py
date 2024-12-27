
def word_counter (str):
    counter = 0
    words = str.split()
    for word in words:
        counter += 1
    return counter

def char_counter(str):
    lower_str = str.lower()
    counter = {}

    for char in str:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 0
    
    return counter

#def key_sort(dic):
   # return di

with open("books/frankenstein.txt") as f:
    file_contents =f.read()
    words = word_counter(file_contents)
    chars = char_counter(file_contents)
    #chars.sort(reverse = true)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} found in the document")

    for w in sorted(chars, key = chars.get, reverse = True):
        print(f"the {w} was found {chars[w]} times")

    #for char in chars:
    #   value = chars[char]
    #   print(f"the {char} was found {value} times")
    print("end report")