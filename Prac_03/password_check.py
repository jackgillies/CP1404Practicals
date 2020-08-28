MINIMUM_LENGTH = 4


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asteriks(password)


def get_password(minimum_length):
    password = input("Enter Password of at Least {} Characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter Password of at Least {} Characters: ".format(minimum_length))
    return password


def print_asteriks(password):
    print('*' * len(password))


main()
