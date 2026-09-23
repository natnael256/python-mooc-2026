# when except is use as a blanket it will also hide a syntax errors. 

# Write your solution here
# try:
#     with open("src/text.txt") as my_file:

#         for line in myfile:
#             print(line)
# except: 
#     print("There was an error when reading the file.")

# with open("src/text.txt") as my_file:

#     for line in my_file:
#         print(line)


def new_person(name_input: str, age: int):

    return_data = ()
    name_content = name_input.split(" ")
    print (name_content)
    print(len(name_content))
    print(len(name_input))


    
    if len(name_content) < 2  or len(name_input) > 40:
        raise ValueError ("The input is invalid")

    if age < 0 or age > 150:
        raise ValueError ("The input is invalid")
        
    return_data = (name_input, age)
    return(return_data)


if __name__ == "__main__":
    new_person('James Jameson', 32)