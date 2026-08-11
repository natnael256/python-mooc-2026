# Write your solution here


def invert(dic: dict):

    new_dic = {}
    
    for key in dic.keys():

        j = dic.get(key)

        new_dic[j] = key

    dic.clear()
    dic.update(new_dic)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)