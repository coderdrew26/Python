def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    Stuart, Kevin = 0, 0
    length = len(string)
    for i in range(length):
        score = length - i
        if string[i] in vowels:
            Kevin += score
        else:
            Stuart += score
    if Stuart == Kevin:
        print("Draw")
    if Stuart > Kevin:
        print("Stuart {}".format(Stuart))
    if Stuart < Kevin:
        print("Kevin {}".format(Kevin))
if __name__ == '__main__':
    s = input()
    minion_game(s)