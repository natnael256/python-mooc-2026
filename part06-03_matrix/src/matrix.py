# write your solution here
def read_file():
    new_mat = []

# read the file 
    with open("src/matrix.txt", "r", encoding="utf-8") as mat:
    
# row loop 
        for i in mat: 
            # row to hold teh clane num
            row = []
            for j in i.split(","):

                if j.strip() != "":
                    number = int(j)
                    row.append(number)
        
            new_mat.append(row)
        return new_mat


# print(matrix_txt)




def row_sums():
    matrix_txt = read_file()
    row_sum = []

    for i in matrix_txt:

        row_sum.append(sum(i))

    return row_sum


# print("_______________________")
# print(row_sums())

        


def matrix_sum():
    matrix_txt = read_file()
    matrix_sum  = 0 
    for i in matrix_txt:

        matrix_sum = sum(row_sums())

    return matrix_sum

def matrix_max():
    matrix_txt = read_file()

    max_num = 0

    new_list = []
    for i in range(len(matrix_txt)):

        for j in range(len(matrix_txt)):

            new_list.append(matrix_txt[i][j])

    max_num = max(new_list)
    
    return max_num


# print("_______________________")
# print(matrix_sum())


# print("_______________________")
# print(matrix_max())


