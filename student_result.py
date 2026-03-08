def main():
    # Ask for student's name
    name = input("Enter student's name: ")

    # Ask for 3 subject marks
    try:
        mark1 = float(input("Enter marks for subject 1: "))
        mark2 = float(input("Enter marks for subject 2: "))
        mark3 = float(input("Enter marks for subject 3: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
        return

    # Calculate the average
    average = (mark1 + mark2 + mark3) / 3

    # Display the result
    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    main()
