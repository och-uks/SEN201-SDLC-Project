#Project: Student Grade Calculator
# Nomenclature matches SDLC Design Phase in documentation

def main():
    print("--- Student Grade Calculator ---")
    
    try:
        # Phase 2 Design Name: score
        # Requirement: Take a numerical score from a student
        score = float(input("Enter the numerical score: "))

        if score < 0 or score > 100:
            print("Error: Please enter a score between 0 and 100.")
            return

        # Phase 2 Design Names: letter_grade, grade_point
        # Implementation of Grading Logic
        if score >= 70:
            letter_grade = "A"
            grade_point = 5
        elif score >= 60:
            letter_grade = "B"
            grade_point = 4
        elif score >= 50:
            letter_grade = "C"
            grade_point = 3
        elif score >= 45:
            letter_grade = "D"
            grade_point = 2
        else:
            letter_grade = "F"
            grade_point = 0

        # Phase 4: Testing/Output
        print("\n--- Result Analysis ---")
        print(f"Numerical Score: {score}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Grade Point: {grade_point}")

    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
