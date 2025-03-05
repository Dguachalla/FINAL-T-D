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


def get_user_input():
    """
    Get user input for weight and height.
    """
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None


def main():
    """
    Main function to run the BMI calculator.
    """
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    if weight and height:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"Your BMI is {bmi:.2f}, which is classified as {category}.")


if __name__ == "__main__":
    main()