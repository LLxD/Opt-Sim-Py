import random

def play_game(p, money=50, multiplying_factor=2):
    games = 0
    initial_money = money
    while money > 0 and money < (initial_money * multiplying_factor):
        games += 1
        if random.random() < p:
            money += 1
        else:
            money -= 1
    if money == (initial_money * multiplying_factor):
        return [True, games]
    else:
        return [False, games]


def main():
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        games = 0
        for i in range(1000):
            result = play_game(p)
            if result[0]:
                games += result[1]
        if ((games/1000) == 0):
            print("p = " + str(p) + " average games to win = Never")
        else:
            print("p = " + str(p) + " average games to win = " + str(games / 1000))


if __name__ == "__main__":
    main()