#print("hello world")

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book(book_path) #read book into text
    word_count = get_word_count(text) #takes text, splits into list of words, return list length
    letter_counts = get_letter_counts(text) #takes text, counts each letter into a dict, return dict
    letter_list = alpha_sort(letter_counts) #takes dict, if key is alphabet, add to list as (amount,key), sort list, return list
    
    print("-----begin book report-----")
    print()
    print("start word report")
    print(f"{word_count} words in book")
    print("end word report")
    print()
    print("start letter report")
    for i in range(len(letter_list)-1,-1,-1):
        print(f'{letter_list[i][0]}x "{letter_list[i][1]}"')
    print("end letter report")
    print()
    print("-----end report-----")
    
def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def alpha_sort(letter_counts):
    letter_list = []
    for letter in letter_counts:
        if letter.isalpha():
            tuple1 = (letter_counts[letter], letter)
            letter_list.append(tuple1)
    letter_list.sort() #how do i sort in descending?
    return letter_list

def get_letter_counts(text):
    letters = {}
    for letter in text:
        c = letter.lower()
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def get_book(book_path):
    with open(book_path) as file:
        return file.read()

main()