# Write your solution here

# Write your solution here


def add_movie(database: list, name: str, director:str, year: int, runtime: int):
    new_bd = {}

    if len(new_bd) < 1:
        new_bd["name"] = name
        new_bd["director"] = director
        new_bd["year"] = year
        new_bd["runtime"] = runtime
    else:
        new_bd["name"].append(name)
        new_bd["director"].append(director)
        new_bd["year"].append(year)
        new_bd["runtime"].append(runtime)

    database.append(new_bd)





if __name__ == "__main__":

    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)