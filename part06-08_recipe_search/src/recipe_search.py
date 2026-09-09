# Write your solution here
# file_name = "src/recipes1.txt"

# file_name = input("What is the file name: ")
# recipe_name_s = input("What is the recipe you are trying to find: ")



def file_open(file_name: str):
    recipes = {}
    with open(file_name, "r") as recipes_list:
        # with open("src/recipes1.txt", "r") as recipes_list:
        text = recipes_list.read()

    for i in text.split("\n\n"):

        line = i.strip()
        word_in_line = i.splitlines()

        recipe_name = word_in_line[0]

        recipes[recipe_name] = word_in_line[1:]
    return recipes


def search_by_name(filename: str, recipe_name: str):
    recipes = file_open(filename)
    result = []
    for key in recipes:

        if recipe_name.lower() in key.lower():
            # print(f"{key}")
            result.append(key)
    return result

def search_by_time(filename: str, prep_time: int):
    recipes = file_open(filename)
    result = []
    # time = str(prep_time)

    for i, values in recipes.items():

        if int(values[0]) <= prep_time:
            # print(f"{i}, preparation time {values[0]} min")
            result.append(f"{i}, preparation time {values[0]} min")

    return result

def search_by_ingredient(filename: str, ingredient: str):
    recipes = file_open(filename)
    result = []
    for i, values in recipes.items():

        if ingredient in values:
            # print(f"{i}, preparation time {values[0]} min")
            result.append(f"{i}, preparation time {values[0]} min")

    return result

if __name__ == "__main__":

    file_name = "src/recipes2.txt"
    recipe_name_s = "cake"
    input_time =5
    ingredient_input = "eggs"
    print("by name")
    print(search_by_name(file_name, recipe_name_s))
    print("by time")
    print(search_by_time(file_name, input_time))
    print("by ingredient")
    print(search_by_ingredient(file_name, ingredient_input))
