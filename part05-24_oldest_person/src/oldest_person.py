# Write your solution here

def oldest_person(people: list):


    age = 0
    name = ""

    for tup in people:

        test_age = 2026 - tup[1]
        if test_age > age:
            age = test_age
            name = tup[0]

    return name
        

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))


