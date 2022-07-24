import random

friend_amount = int(input("Enter the number of friends joining (including you): \n > "))

if friend_amount > 0:
    friend_dict = {}

    print("\nEnter the name of every friend (including you), each on a new line:")

    for _ in range(friend_amount):
        # set default checks if first argument is in dict, if not adds it as the key with default value of None
        friend_dict.setdefault(input("> "), 0)

    total_bill = float(input("\nEnter the total bill value:\n> "))

    response = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n> ').lower()
    if response == 'yes':
        names = [name for name in friend_dict]
        winner = random.choice(names).title()
        print(f"\n{winner} is the lucky one!\n")

        individual_bill = round(total_bill / (friend_amount-1), 2)

        for friend in friend_dict:
            if friend.title() != winner:
                friend_dict[friend] = individual_bill

        print(friend_dict)
    else:
        individual_bill = round(total_bill / friend_amount, 2)

        for friend in friend_dict:
            friend_dict[friend] = individual_bill

        print("\nNo one is going to be lucky\n")
        print(friend_dict)
else:
    print("No one is joining for the party")


