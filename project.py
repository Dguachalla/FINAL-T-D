def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (kg) and height (m).
    Formula: BMI = weight / (height ** 2)
    """
    if height <= 0:
        raise ValueError("Height must be greater than 0.")
    return weight / (height ** 2)


def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def get_exercise_recommendation(category):
    """
    Provide exercise recommendations based on BMI category.
    """
    recommendations = {
        "Underweight": {
            "Beginner": ["Bodyweight squats", "Push-ups (knee-assisted)", "Walking"],
            "Intermediate": ["Weightlifting", "Yoga", "Cycling"],
            "Advanced": ["Strength training", "HIIT", "Swimming"]
        },
        "Normal weight": {
            "Beginner": ["Walking", "Light jogging", "Stretching"],
            "Intermediate": ["Running", "Cycling", "Bodyweight exercises"],
            "Advanced": ["CrossFit", "Weightlifting", "Martial arts"]
        },
        "Overweight": {
            "Beginner": ["Walking", "Swimming", "Yoga"],
            "Intermediate": ["Cycling", "Elliptical training", "Light weightlifting"],
            "Advanced": ["Running", "Circuit training", "Aerobics"]
        },
        "Obesity": {
            "Beginner": ["Chair exercises", "Water aerobics", "Stretching"],
            "Intermediate": ["Walking", "Stationary cycling", "Light yoga"],
            "Advanced": ["Low-impact aerobics", "Swimming", "Resistance band exercises"]
        }
    }
    return recommendations.get(category, "No recommendations available.")


def get_diet_suggestions(category):
    """
    Provide diet suggestions based on BMI category.
    """
    suggestions = {
        "Underweight": {
            "Macronutrient Balance": "Increase calorie intake with a focus on proteins and healthy fats.",
            "Tips": [
                "Eat calorie-dense foods like nuts, seeds, and avocados.",
                "Include protein-rich foods like eggs, chicken, and legumes.",
                "Have frequent small meals throughout the day."
            ]
        },
        "Normal weight": {
            "Macronutrient Balance": "Maintain a balanced diet with equal portions of carbs, proteins, and fats.",
            "Tips": [
                "Eat a variety of fruits and vegetables.",
                "Include whole grains and lean proteins.",
                "Limit processed foods and sugary drinks."
            ]
        },
        "Overweight": {
            "Macronutrient Balance": "Reduce calorie intake with a focus on lean proteins and complex carbs.",
            "Tips": [
                "Avoid sugary and processed foods.",
                "Increase fiber intake with vegetables and whole grains.",
                "Drink plenty of water and avoid sugary drinks."
            ]
        },
        "Obesity": {
            "Macronutrient Balance": "Focus on portion control and nutrient-dense foods.",
            "Tips": [
                "Consult a dietitian for a personalized plan.",
                "Avoid fried and high-calorie foods.",
                "Incorporate more vegetables and lean proteins into your diet."
            ]
        }
    }
    return suggestions.get(category, "No diet suggestions available.")


def get_user_input():
    """
    Get user input for weight and height with validation.
    """
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be greater than 0. Please try again.")
            else:
                return weight, height
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def display_menu():
    """
    Display a menu for the user to choose options.
    """
    print("\nBMI Calculator Menu:")
    print("1. Calculate BMI")
    print("2. Get Exercise Recommendations")
    print("3. Get Diet Suggestions")
    print("4. Exit")


def main():
    """
    Main function to run the BMI calculator with enhanced features.
    """
    print("Welcome to the Enhanced BMI Calculator!")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"\nYour BMI is {bmi:.2f}, which is classified as {category}.")

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"\nYour BMI is {bmi:.2f}, which is classified as {category}.")
        elif choice == "2":
            print("\nExercise Recommendations:")
            exercises = get_exercise_recommendation(category)
            for level, activities in exercises.items():
                print(f"{level}: {', '.join(activities)}")
        elif choice == "3":
            print("\nDiet Suggestions:")
            diet = get_diet_suggestions(category)
            print(f"Macronutrient Balance: {diet['Macronutrient Balance']}")
            print("Tips:")
            for tip in diet["Tips"]:
                print(f"- {tip}")
        elif choice == "4":
            print("Thank you for using the BMI Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()