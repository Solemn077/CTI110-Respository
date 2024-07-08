def get_positive_integer():
    while True:
        try:
            num = int(input("Enter a integer: "))
            if num >= 0:
                return num
            else:
                print("Sorry, I cannot accept negative values. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def display_multiplication_table(num):
    print(f"Multiplication table for {num} from 1 to 12:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def main():
    while True:
        user_num = get_positive_integer()
        display_multiplication_table(user_num)
        repeat = input("Do you want to run it again? (yes/no): ").lower()
        if repeat != "yes":
            break

if __name__ == "__main__":
    main()
