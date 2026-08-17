# write your solution here


def read_fruits():
    
    fruits_dict = {}
    with open("fruits.csv", "r", encoding="utf-8") as fruits:
    # with open("src/fruits.csv", "r", encoding="utf-8") as fruits:

        for i in fruits:
            i = i.replace("\n", "")

            fruit = i.split(";")

            fruit_name = fruit[0]
            price = round(float(fruit[1]),2)


            fruits_dict [fruit_name] = price
    return fruits_dict

# print(read_fruits())

