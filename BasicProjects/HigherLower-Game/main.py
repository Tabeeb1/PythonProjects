import random
import art
import data
data = data.data
score = 0
while True:
    A = random.choice(data)
    B = random.choice(data)

    while A["name"] == B["name"]:
        B = random.choice(list(data.values()))
    if score == 0:
        print(art.logo)
        print(f'Compare A: {A["name"]}, a {A["description"]} from {A["country"]}')
        print(art.vs)
        print(f'Compare B: {B["name"]}, a {B["description"]} from {B["country"]}')

        follow = input("Who has more followers? Type A or B: ")
        if follow == 'A' and A["follower_count"] > B["follower_count"]:
            score += 1
        elif follow == 'B' and B["follower_count"] > A["follower_count"]:
            score += 1
        else:
            print(f'Sorry, that"s wrong. Final score: {score}')
            break
    else:
        print(art.logo)
        print(f'You"re right! Current score: {score}.')
        print(f'Compare A: {A["name"]}, a {A["description"]} from {A["country"]}')
        print(art.vs)
        print(f'Compare B: {B["name"]}, a {B["description"]} from {B["country"]}')

        follow = input("Who has more followers? Type A or B: ")
        if follow == 'A' and A["follower_count"] > B["follower_count"]:
            score += 1
        elif follow == 'B' and B["follower_count"] > A["follower_count"]:
            score += 1
        else:
            print(f'Sorry, that"s wrong. Final score: {score}')
            break

