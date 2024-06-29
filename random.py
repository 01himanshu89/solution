import random

def generate_random_numbers():
    print("Random Number Generator")
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        count = int(input("Enter the number of random numbers to generate: "))

        if lower_bound > upper_bound:
            print("The lower bound cannot be greater than the upper bound.")
            return

        print(f"\nGenerating {count} random numbers between {lower_bound} and {upper_bound}:")
        random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(count)]
        for num in random_numbers:
            print(num)

    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Call the function to run the program
generate_random_numbers()
