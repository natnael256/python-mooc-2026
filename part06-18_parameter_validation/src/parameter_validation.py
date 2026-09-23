

with open ("src/lottery_numbers.csv") as my_file:

    content = []
    for line in my_file:
        line = line.strip()
        value = line.split(';')
        content.append(value)

valid = []
final_valid = []



for i in content:
    skip =False
    for j in i[0].split(" "):
        try:
            week_num = int(j[2])
        except ValueError:
            pass
            skip = True
            break
    num_part = i[1].replace(',','')
    if skip == False and len(num_part) == 7:
        if num_part.isdigit():
            final_valid.append(i)
    print(final_valid)
        