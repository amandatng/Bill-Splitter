import tkinter as tk

window = tk.Tk()
window.title("Bill Splitter")
window.geometry("800x800")

all_prices = []
price_list = []
name_entries = []
bill_grid = []
check_boxes = []
int_vars = []


# adds a new name, adjusts checkboxes
def add_person():
    name_box = tk.Entry(window, width = 7)
    name_entries.append(name_box)
    length = len(name_entries)
    name_box.grid(row = 2, column = length + 3)
    add_person_b.grid(row = 2, column = length + 4)

    price_len = len(all_prices)
    check_col = []
    var_col = []
    if price_len != 0:
        for num in range(price_len):
            tester = tk.IntVar()
            check_b = tk.Checkbutton(window, variable = tester)
            check_boxes[num].append(check_b)
            int_vars[num].append(tester)
            check_b.grid(row = num + 3, column = length + 3)

        check_col.clear()
        var_col.clear()

# grab the people's name and add it to an array
def get_person():
    length = len(name_entries)
    names = []
    for num in range(length):
        name = name_entries[num].get()
        names.extend([name])
    bill_grid.extend([names])
    names = []

# add price field, adjust checkboxes
def add_price():
    price_box = tk.Entry(window)
    all_prices.append(price_box)
    length = len(all_prices)
    price_box.grid(row = length + 2, column = 2)
    add_price_b.grid(row = length + 3, column = 2)
    check_row = []
    var_row = []

    person_len = len(name_entries)
    if person_len != 0:
        for num in range(person_len):
            tester = tk.IntVar()
            check_b = tk.Checkbutton(window, variable = tester)
            check_row.append(check_b)
            var_row.append(tester)
            check_b.grid(row = length + 2, column = num + 4)
        check_boxes.extend([check_row])
        int_vars.extend([var_row])
    else:
        check_boxes.extend([[]])
        int_vars.extend([[]])

#count number of boxes checked
def count_checks():
    length = len(int_vars)
    print(length)
    for num in length:
        row_len = len(int_vars[num])
        for j in row_len:
            state = int_vars[j].get()

# grab prices from price fields
def get_price():
    length = len(all_prices)
    for num in range(length):
        curr_price = all_prices[num].get()
        price_list.extend(curr_price)
        print(curr_price)


window.rowconfigure(1, {'minsize' : 30})
window.columnconfigure(1, {'minsize' : 30})
add_person_b = tk.Button(window, text = "add person", width = 10, command = add_person)
add_person_b.grid(row = 2, column = 3)
submit_b = tk.Button(window, text = "submit person", width = 10, command = count_checks)
submit_b.grid(row = 10, column = 10)
add_price_b = tk.Button(window, text = "add price", width = 10, command = add_price)
price_len = len(all_prices)
add_price_b.grid(row = 3, column = 2)

window.mainloop()
