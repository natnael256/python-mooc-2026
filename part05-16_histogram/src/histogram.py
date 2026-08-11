# Write your solution here

def histogram(word):

    count = {}


    for i in word:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for j in count:

        print (f"{j} {count[j] * '*'}")


if __name__ == "__main__":

    word = "statistically"

    histogram(word)

