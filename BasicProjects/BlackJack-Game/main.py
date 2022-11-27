import art
import random
import value

def give_card(llist_values,first_value,second_value,computer_first_value):
    third_value = random.choice(list(llist_values.values()))
    if first_value + second_value + third_value > 21:
        third_value = 1
    total = first_value + second_value + third_value
    print(f'Your cards: [{first_value}, {second_value}, {third_value}], current score: {total}')
    print(f"computer's first card: {computer_first_value}")
    print(f'Your final hand: [{first_value}, {second_value}, {third_value}], final score: {total}')
    computer_second_value = random.choice(list(llist_values.values()))
    if computer_first_value + computer_second_value < 17:
        computr_third_value = random.choice(list(llist_values.values()))
        computer_total = computer_first_value + computer_second_value + computr_third_value
        print(
            f"Computer's final hand: [{computer_first_value}, {computer_second_value}, {computr_third_value}], final score: {computer_total}")

    else:
        computer_total = computer_first_value + computer_second_value
        print(f"Computer's final hand: [{computer_first_value}, {computer_second_value}], final score: {computer_total}")
    if computer_total > 21 and total > 21:
        print("Draw due to both being over 21")
    elif computer_total < 21 and total > 21:
        print("You went over. You lose")
    elif computer_total > 21 and total < 21:
        print("You win because computer went over")
    elif computer_total > total:
        print("You lose because computer has more point")
    elif total > computer_total:
        print("You win because you have more point")

def not_give_card(llist_values,first_value,second_value,computer_first_value):
    total = first_value + second_value
    print(f'Your final hand: [{first_value}, {second_value}], final score: {total}')
    computer_second_value = random.choice(list(llist_values.values()))
    computer_total = 0
    if computer_first_value + computer_second_value < 17:
        computr_third_value = random.choice(list(llist_values.values()))
        computer_total = computer_first_value + computer_second_value + computr_third_value
        print(
            f"Computer's final hand: [{computer_first_value}, {computer_second_value}, {computr_third_value}], final score: {computer_total}")

    else:
        computer_total = computer_first_value + computer_second_value
        print(f"Computer's final hand: [{computer_first_value}, {computer_second_value}], final score: {computer_total}")
    if computer_total > 21 and total > 21:
        print("Draw due to both being over 21")
    elif computer_total < 21 and total > 21:
        print("You went over. You lose")
    elif computer_total > 21 and total < 21:
        print("You win because computer went over")
    elif computer_total > total:
        print("You lose because computer has more point")
    elif total > computer_total:
        print("You win because you have more point")


print(art.logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'n':
    pass
else:
    while play == 'y':
        llist_values = value.llist_values
        first_value = random.choice(list(llist_values.values()))
        second_value = random.choice(list(llist_values.values()))
        if first_value + second_value > 21:
            if first_value == 11 and second_value == 11:
                first_value = 1

        print(f'Your cards: [{first_value} , {second_value}], current score: {first_value+second_value}')
        computer_first_value = random.choice(list(llist_values.values()))
        print(f"Computer's first card: {computer_first_value}")
        pass_play = input("Type 'y' to get another card, type 'n' to pass: ")
        if pass_play == 'y':
            give_card(llist_values,first_value,second_value,computer_first_value)
        else:
            not_give_card(llist_values,first_value,second_value,computer_first_value)
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
