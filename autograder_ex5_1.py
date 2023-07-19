def get_integer_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'done':
                return None
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'done'.")

def main():
    smallest = None
    largest = None

    while True:
        num = get_integer_input("Enter an integer number (type 'done' to finish): ")
        if num is None:
            break

        if smallest is None or num < smallest:
            smallest = num

        if largest is None or num > largest:
            largest = num

    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")

if __name__ == "__main__":
    main()
