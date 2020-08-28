MENU_STRING = "(E)ven\n(O)dd\n(S)quare\n(Q)uit"
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))
print(MENU_STRING)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "E":
        for i in range(first_number, second_number + 1):
            if i % 2 == 0:
                print(i, end =' ')
    elif menu_choice == "O":
        for i in range(first_number, second_number + 1):
            if i % 2 != 0:
                print(i, end =' ')
    elif menu_choice == "S":
        for i in range(first_number, second_number + 1):
            print(i**2)
    else:
        print("Invalid ")
        print(MENU_STRING)
    menu_choice = input(">>>").upper()
print("Finished.")