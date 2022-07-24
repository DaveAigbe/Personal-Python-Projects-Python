x = ['_','_','_','_','_','_','_','_','_']

global y
global z
global c
y = x[0:3]
z = x[3:6]
c = x[6:]

counter = 1
X_or_O = 'X'
keep_playing = 1

def update_grid():
    print("---------")
    print('|', ' '.join(y), '|')
    print('|', ' '.join(z), '|')
    print('|', ' '.join(c), '|')
    print("---------")


update_grid()  # updates grid each time something changes



while keep_playing == 1:

    def valid_input():
        global list_coordinates  # so that the variable can be used outside of its else statement
        valid = False  # set valid to false so that while will run as long as the input is invalid

        while valid == False:  # while the conditions return false(if proper input they will return true)
            cd = input('Please enter coordinates: ').replace(' ','')  # take input each time it is looped and remove whitespace
            valid = cd.isnumeric()  # valid will return true if user entered number otherwise it will be set to false
            if valid == False:  # if valid returned false the user did not even enter a number
                print('Please enter a number!')
            else:
                list_coordinates = [int(v) for v in cd]  # put numbers into list and set them as ints
                print(list_coordinates)# display the new list, at this point valid is still true
                if not (0 < list_coordinates[0] <= 3 and 0 < list_coordinates[1] <= 3):  # if coordinates are not in the range of 1-3, set valid to false which will run the loop again
                    print('Coordinates should be from 1 to 3!')
                    valid = False
                else:
                    if list_coordinates[0] == 1:#checks the row
                        if y[list_coordinates[1]-1] != '_':#checks the column spot for whitespace
                            print('This cell is occupied! Choose another one!')#if there is not a whitespace rerun function
                            valid = False
                    elif list_coordinates[0] == 2:
                        if z[list_coordinates[1] - 1] != '_':
                            print('This cell is occupied! Choose another one!')
                            valid = False
                    elif list_coordinates[0] == 3:
                        if c[list_coordinates[1] - 1] != '_':
                            print('This cell is occupied! Choose another one!')
                            valid = False
                    while valid == True:
                        return list_coordinates  # if the input passed all the conditions return it as a valid input


    final_input = valid_input() #final input should be the list that returned from valid_input function
    # if coordinate is not whitespace print This cell is occupied! Choose another one!

    if final_input[0] == 1: #this is the row it will be in
        y[final_input[1] - 1] = X_or_O #column it will be in, minus one because index start from 0 (0,1,2) rather than (1,2,3)
        update_grid()
    elif final_input[0] == 2:
        z[final_input[1] - 1] = X_or_O
        update_grid()
    elif final_input[0] == 3:
        c[final_input[1] - 1] = X_or_O
        update_grid()

    def draw_check():
        check = 0

        for i in y + z + c:
            if i != '_':
                check += 1
        if check == 9:
            return True
        else:
            return False

    its_a_draw = draw_check()





    if (y[0] == z[0] == c[0]) and y[0] !='_':  # next 3 check for vertical win
        print(f'{y[0]} wins')
        keep_playing = 0
    elif (y[1] == z[1] == c[1]) and y[1] !='_':
        print(f'{y[1]} wins')
        keep_playing = 0
    elif (y[2] == z[2] == c[2]) and y[2] !='_':
        print(f'{y[2]} wins')
        keep_playing = 0
    elif (y[0] == z[1] == c[2]) and y[0] !='_':  # diagonal from first pt
        print(f'{y[0]} wins')
        keep_playing = 0
    elif (y[2] == z[1] == c[0]) and y[2] !='_':  # diagonal from second pt
        print(f'{y[2]} wins')
        keep_playing = 0
    elif (y[0] == y[1] == y[2]) and y[0] !='_':  # next 3 check for horizontal win
        print(f'{y[0]} wins')
        keep_playing = 0
    elif (z[0] == z[1] == z[2]) and z[0] !='_':
        print(f'{z[0]} wins')
        keep_playing = 0
    elif (c[0] == c[1] == c[2]) and c[0] !='_':
        print(f'{c[0]} wins')
        keep_playing = 0
    elif its_a_draw:
        print('Draw')
        break
    elif '_' in x or ' ' in x:
        print("Game not finished")
        if counter == 1:
            X_or_O = 'O'
            counter -= 1
        elif counter == 0:
            X_or_O = 'X'
            counter += 1


