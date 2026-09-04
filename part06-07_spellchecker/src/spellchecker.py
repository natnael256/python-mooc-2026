# write your solution here

words = input("Write text: ")
input_words = words.split()


word_list = []

with open ("src/wordlist.txt") as check_list:



    for i in check_list: 
    
        line = i.strip()
        
        one_word_file = line.split("/n")
        
        word_list.extend(one_word_file)



final_word = ""

# print(input_words)

for i in input_words: 
    word = i.lower()
    if word in word_list:

        final_word = final_word + " " + i
        
    else:  
        final_word = final_word + " " + "*"+ i + "*"
        


print (final_word)


# print(word_list[3:10])