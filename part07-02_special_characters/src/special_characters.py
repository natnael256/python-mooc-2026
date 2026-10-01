# Write your solution here
import string



def separate_characters(my_string: str):

    parts = my_string

    ascii_letters = "". join([i for i in parts if i in string.ascii_letters])

    panct = "".join([i for i in parts if i in string.punctuation])

    all_other = "".join([i for i in parts if i not in string.ascii_letters and i not in string.punctuation])
    # print(f"{ascii_letters}")
    # print(panct)
    # print(all_other)
    return ascii_letters, panct, all_other

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])