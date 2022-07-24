x = list(input("Enter 9 Values: "))

global y
global z
global c
y = x[0:3]
z = x[3:6]
c = x[6:]


def update_grid():
    print("---------")
    print('|', ' '.join(y), '|')
    print('|', ' '.join(z), '|')
    print('|', ' '.join(c), '|')
    print("---------")


update_grid()  # updates grid each time something changes


duplicate_List = x.copy()

for i in duplicate_List:
    if '_' in duplicate_List:
        duplicate_List.remove('_')

numbers_of_XvsO = {duplicate_List.count(i) for i in duplicate_List}
set_to_list = [n for n in numbers_of_XvsO]
unique_number_count = [set_to_list.count(y) for y in set_to_list]


if (sum(unique_number_count) == 1) and ('_' in x or ' ' in x):
    if (y[0] == z[0] == c[0]) and (y[1] == z[1] == c[1]):  # next 3 check says its impossible that 2 verticals win
        print(f'Impossible')
    elif (y[1] == z[1] == c[1]) and (y[2] == z[2] == c[2]):
        print(f'Impossible')
    elif (y[0] == z[0] == c[0]) and (y[2] == z[2] == c[2]):
        print(f'Impossible')
    elif y[0] == y[1] == y[2] and z[0] == z[1] == z[2]:  # next 3 check says its impossible that 2 horizontals win
        print(f'Impossible')
    elif z[0] == z[1] == z[2] and c[0] == c[1] == c[2]:
        print(f'Impossible')
    elif y[0] == y[1] == y[2] and c[0] == c[1] == c[2]:
        print(f'Impossible')
    elif y[0] == z[0] == c[0]:  # next 3 check for vertical win
        print(f'{y[0]} wins')
    elif y[1] == z[1] == c[1]:
        print(f'{y[1]} wins')
    elif y[2] == z[2] == c[2]:
        print(f'{y[2]} wins')
    elif y[0] == z[1] == c[2]:  # diagonal from first pt
        print(f'{y[0]} wins')
    elif y[2] == z[1] == c[0]:  # diagonal from second pt
        print(f'{y[2]} wins')
    elif y[0] == y[1] == y[2]:  # next 3 check for horizontal win
        print(f'{y[0]} wins')
    elif z[0] == z[1] == z[2]:
        print(f'{z[0]} wins')
    elif c[0] == c[1] == c[2]:
        print(f'{c[0]} wins')
    elif '_' or " " in x:  # checks for whitespace
        print("Game not finished")
    elif '_' or " " not in x:  # if there is no whitespace and no one has won yet
        print('Draw')
elif (set_to_list[1] - set_to_list[0]) > 1:
    print(f'Impossible')
elif (y[0] == z[0] == c[0]) and (y[1] == z[1] == c[1]):  # next 3 check says its impossible that 2 verticals win
    print(f'Impossible')
elif (y[1] == z[1] == c[1]) and (y[2] == z[2] == c[2]):
    print(f'Impossible')
elif (y[0] == z[0] == c[0]) and (y[2] == z[2] == c[2]):
    print(f'Impossible')
elif y[0] == y[1] == y[2] and z[0] == z[1] == z[2]:  # next 3 check says its impossible that 2 horizontals win
    print(f'Impossible')
elif z[0] == z[1] == z[2] and c[0] == c[1] == c[2]:
    print(f'Impossible')
elif y[0] == y[1] == y[2] and c[0] == c[1] == c[2]:
    print(f'Impossible')
elif y[0] == z[0] == c[0]:  # next 3 check for vertical win
    print(f'{y[0]} wins')
elif y[1] == z[1] == c[1]:
    print(f'{y[1]} wins')
elif y[2] == z[2] == c[2]:
    print(f'{y[2]} wins')
elif y[0] == z[1] == c[2]:  # diagonal from first pt
    print(f'{y[0]} wins')
elif y[2] == z[1] == c[0]:  # diagonal from second pt
    print(f'{y[2]} wins')
elif y[0] == y[1] == y[2]:  # next 3 check for horizontal win
    print(f'{y[0]} wins')
elif z[0] == z[1] == z[2]:
    print(f'{z[0]} wins')
elif c[0] == c[1] == c[2]:
    print(f'{c[0]} wins')
elif '_' in x or ' ' in x:  # checks for whitespace
    print("Game not finished")
elif '_' in x or ' ' not in x:  # if there is no whitespace and no one has won yet
    print('Draw')
