from tkinter import *
import datetime

FONT_NAME = 'Helvetica'

# Window
window = Tk()
window.title("Age Calculator")
window.config(bg='white')

# Canvas with Image
canvas = Canvas(width=320, height=225, bg='white', highlightthickness=0)
life_img = PhotoImage(file='ages.png')
canvas.create_image(145, 113, image=life_img)
canvas.grid(column=1, row=0)

# Text Boxes
name_box = Entry(width=30)
name_box.grid(column=1, row=1, pady=5)

year_box = Entry(width=30)
year_box.grid(column=1, row=2, pady=5)

month_box = Entry(width=30)
month_box.grid(column=1, row=3, pady=5)

day_box = Entry(width=30)
day_box.grid(column=1, row=4, pady=5)

# Text Box Labels
name_label = Label(text='Name', bg='white', fg='black', font=(FONT_NAME, 10, "bold"))
name_label.grid(column=0, row=1)

year_label = Label(text='Year', bg='white', fg='black', font=(FONT_NAME, 10, "bold"))
year_label.grid(column=0, row=2)

month_label = Label(text='Month', bg='white', fg='black', font=(FONT_NAME, 10, "bold"))
month_label.grid(column=0, row=3)

day_label = Label(text='Day', bg='white', fg='black', font=(FONT_NAME, 10, "bold"))
day_label.grid(column=0, row=4)

answer_label = Label(text='', bg='white', fg='black', font=(FONT_NAME, 10, "bold"))
answer_label.grid(column=1, row=5)


# Calculate Input
def calculate():
    year = int(year_box.get())
    month = int(month_box.get())
    day = int(day_box.get())
    name = name_box.get()

    user_date = datetime.date(year, month, day)
    current_date = datetime.date.today()

    # Calculate differences to get age
    year_diff = current_date.year - user_date.year
    month_diff = current_date.month - user_date.month
    day_diff = current_date.day - user_date.day

    # Eliminate negatives
    if month_diff < 0:
        month_diff = month_diff + 12
    elif day_diff < 0:
        day_diff = day_diff + 30

    # Create empty sentence
    formatted_string = f'{name.title()} is '

    # Add phrases to sentence
    if year_diff == 0:
        pass
    elif year_diff == 1:
        formatted_string += f"{year_diff} year"
    else:
        formatted_string += f"{year_diff} years"

    if month_diff == 0:
        pass
    elif day_diff == 0:  # If there is no day value say "Year and Month old" instead of Year, Month
        if month_diff == 1:
            formatted_string += f" and {month_diff} month old."
        else:
            formatted_string += f" and {month_diff} months old."
    else:
        if month_diff == 1:
            formatted_string += f", {month_diff} month"
        else:
            formatted_string += f", {month_diff} months"

    if day_diff == 0:
        pass
    elif day_diff == 1:
        formatted_string += f" and {day_diff} day old."
    else:
        formatted_string += f" and {day_diff} days old."

    answer_label.config(text=formatted_string)


# Button
calculate_button = Button(width=12, text='Calculate Age', bg='#e2979c', font=(FONT_NAME, 10, "bold"), command=calculate)
calculate_button.grid(column=1, row=6, pady=20)

# dark_mode = Button( text='🌛︎︎', bg='white', font=(FONT_NAME, 15, "bold"), highlightthickness=0, bd=0)
# dark_mode.grid(column=0,row=5)


# Keep window open and listen for clicks/actions
window.mainloop()
