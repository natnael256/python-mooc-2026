# Write your solution here
input_name = input("Whome should i sign this to: ")
input_file_name = input("Where shall i save it: ")

with open (f"{input_file_name}", "w") as my_file:

    my_file.write(f"Hi {input_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")