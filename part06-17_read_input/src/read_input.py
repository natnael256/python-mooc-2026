# Write your solution here


def read_input(quetion: str,   num_one: int, num_two: int):
    while True:

        try:
            input_num = input(f"{quetion}")

            number = int(input_num)

            if num_one <= number <=num_two:
                return number
            else:
                print (f"You must type in an integer between {num_one} and {num_two}")
        except ValueError:
            print(f"You must type in an integer between {num_one} and {num_two}") 

if __name__ == "__main__":
    result = read_input("Please type in a number: ",3,9)
    print(f"You typed in:",result)