def main():
    print("--- Student Grade Calculator ---")
    print("Type 'Exit' as the student's name to stop the program.\n")
    
    while True:
        # Get student name
        name = input("Enter the student's name: ")
        
        # Check for exit condition
        if name.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        marks = []
        # Get 3 subject marks with validation
        for i in range(1, 4):
            while True:
                try:
                    user_input = input(f"Enter marks for subject {i} (0-100): ")
                    if user_input.lower() == 'exit':
                        print("Exiting program. Goodbye!")
                        return
                    
                    mark = float(user_input)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Error: Marks must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid numerical value or 'Exit'.")

        # Calculate average
        average = sum(marks) / len(marks)
        
        # Determine grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"
        
        # Display results in requested format
        print("-" * 30)
        print(f"Name: {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade: {grade}")
        print("-" * 30 + "\n")

if __name__ == "__main__":
    main()
