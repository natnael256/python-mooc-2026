# Write your solution here

def factorials(n: int):

    factorial = 1


    factorials = {}
    

    for i in range(factorial,n + 1):
        factorial *= i
        factorials[i] = factorial

    return factorials

        






if __name__ == "__main__":
    print(factorials(5))