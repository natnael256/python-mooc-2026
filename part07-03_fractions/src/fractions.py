# Write your solution here


from fractions import Fraction

def fractionate(amount: int):

    result = []

    for i in range(0, amount):

        result.append(Fraction(1,amount))
    
    return result



if __name__ == "__main__":
    print(fractionate(5))
