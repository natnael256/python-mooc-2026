# Write your solution here



def create_tuple(x: int, y: int, z: int):

    num = [x, y, z]


    tuple_num = (min(num), max(num), sum(num))

    return tuple_num


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))