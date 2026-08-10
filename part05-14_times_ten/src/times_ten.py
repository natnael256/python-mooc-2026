# Write your solution here

def times_ten(start_index: int, end_index: int ):

    dectionary = {}

    count = end_index - start_index


    for i in range(start_index, end_index +1 ):

        dectionary[i] = i * 10

    return dectionary


if __name__ == "__main__":
    print(times_ten(3, 6))