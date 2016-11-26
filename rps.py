from random import randint
rps = list("rps")
def rpscomp(x, y):
    if 1 in [x, y] and len(rps) in [x, y]:
        return min(x, y)
    else:
        return max(x, y)
while True:
    play = input("What's your move? ")
    if play in rps:
        play = rps.index(play)
        cpuplay = randint(0, len(rps))
        win = rpscomp(play, cpuplay)
        if win == play:
            print("The player wins!")
        else:
            print("The computer wins!")
