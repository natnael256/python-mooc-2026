# Write your solution here
# with open("src/diary.txt", "a+") as w_file:
#             w_file.seek(0) 
#             content = w_file.read()
#             print(len(content))
#             print(content)


while True:

    print("1 - add an entry, 2 - read entries, 0 - quit ")
    function = input("Function: ")
    
    if function == "0":
        print("Bye now!")
        break
    elif function == "1":
        entry = input("Diary  entry:")
        with open("diary.txt", "a+") as w_file:
            w_file.seek(0) 
            content = w_file.read()
            if len(content) == 0:                
                w_file.write(f"{entry}")
                print("Diary saved")
            else:
                w_file.write(f"\n{entry}")
                print("Diary saved")

            
    elif function == "2":
        print("Entries:")
        with open ("diary.txt", "r") as r_file:
            print(r_file.read())
           
     
