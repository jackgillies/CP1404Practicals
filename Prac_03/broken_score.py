def main():
    user_score = float(input("Score: "))
    determine_score(user_score)


def determine_score(user_score):
    if user_score < 0 or user_score > 100:
        return "Invalid"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

