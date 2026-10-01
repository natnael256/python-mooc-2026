from math import sqrt

# a^2 + b^2 = c^2
def hypotenuse(leg1: float, leg2: float):

    c = (leg1 * leg1) + (leg2 * leg2)
    return sqrt(c)




if __name__ == "__main__":
    print(hypotenuse(3,4)) 
    print(hypotenuse(5,12)) 
    print(hypotenuse(1,1)) 