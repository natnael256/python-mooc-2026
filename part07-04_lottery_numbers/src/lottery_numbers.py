# Write your solution here
from random import randint, choice



def lottery_numbers(amount: int, lower_bound: int, upper_bound:int):

    result_list = []

    for i in range(0, amount):

        num = randint(lower_bound, upper_bound)
        if num not in result_list:
            result_list.append(num)
        else:

            while num not in result_list:
                num = randint(lower_bound, upper_bound)
            result_list.append(num)
 
    return sorted(result_list)

if __name__ == "__main__":

    loto_num = lottery_numbers(7, 1, 40)
    
    print(loto_num)