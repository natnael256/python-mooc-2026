import json





def  print_persons(filename: str):

    with open(filename) as my_file:
        data = my_file.read

    content = json.loads(data)

    return content



if __name__ == "__main__":

    print_persons("src/file1.json")