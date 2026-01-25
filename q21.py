#Write a program to display the month name and number of days using switch-case for a given month number.
month_number=int(input("enter month number:"))

match month_number:
    case 1:
        print(f"january")
    case 2:
        print(f"febuary")
    case 3:
        print(f"march")
    case 4:
        print(f"april")
    case 5:
        print(f"may")
    case 6:
        print(f"june")
    case 7:
        print(f"july")
    case 8:
        print(f"august")
    case 9:
        print(f"september")
    case 10:
        print(f"october")
    case 11:
        print(f"november")
    case 12:
        print(f"december")