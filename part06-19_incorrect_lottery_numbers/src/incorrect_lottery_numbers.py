def filter_incorrect():
    with open ("./lottery_numbers.csv") as my_file:

        content = []
        for line in my_file:
            line = line.strip()
            value = line.split(';')
            content.append(value)

    # print(f"{content}")

    valid_week_side = []
    valid_result = []
    for i in content:
        week_side = i[0].split(" ")
        # print(week_side)
        try:
            week_num = int(week_side[1])
            valid_week_side.append(i)
        except ValueError:
            pass


    # for i in valid_week_side:
    #     print(i)


    for j in valid_week_side:
        loto_part = j[1].split(',')
        # print(f"l_n = {loto_part} length {len(loto_part)}")
        try:
            if len(loto_part) == 7:
                loto_number = [int(num) for num in j[1].split(',')]
                # print(loto_number)
                if max(loto_number) <= 39 and min(loto_number) >= 1:
                    if len(loto_number) == len(set(loto_number)):
                        valid_result.append(j)
        except ValueError:
                    pass


    # for i in valid_result:
    #     # print(i)


    with open("correct_numbers.csv", "w") as my_file:

        for index, i in enumerate(valid_result):

            line = ""

            for val_index, value in enumerate(i):
                if val_index == 0:
                    line += f"{value};"
                else:
                    line += f"{value}"
            if index == len(valid_result) -1:
                my_file.write(line)
            else:
                my_file.write(line + "\n")
            

if __name__ == "__main__":
    filter_incorrect()   