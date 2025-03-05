# Enhanced BMI Calculator
#### Video Demo: <URL (https://www.youtube.com/watch?v=LexmrY6f4qQ)
#### Description:
The **Enhanced BMI Calculator** is a comprehensive and user-friendly Python program meticulously designed to calculate Body Mass Index (BMI) and subsequently provide highly personalized exercise and diet recommendations based on the user's specific BMI category. This innovative project goes beyond a simple BMI calculator by offering actionable health insights, making it a truly invaluable tool for anyone aspiring to improve their overall fitness and nutrition. Users can effectively interact with the program through a conveniently structured menu-driven interface, selecting from a variety of options that allow them to calculate their BMI efficiently, view exercise recommendations tailored to their personal fitness goals, or obtain diet tips specifically crafted for their unique BMI category. Additionally, this program allows users to track their progress over time, helping them stay motivated and informed about their health journey. Overall, the Enhanced BMI Calculator encourages users to take charge of their health by providing them with necessary information and guiding them toward healthier lifestyle choices that can lead to improved wellbeing and long-lasting results. It empowers individuals to make informed decisions and adopt sustainable practices that enhance their quality of life and overall health. 
---

## Features
1. **BMI Calculation**:
   - Calculates BMI using the formula: `BMI = weight (kg) / (height (m))^2`.
   - Classifies BMI into categories: Underweight, Normal weight, Overweight, and Obesity.

2. **Exercise Recommendations**:
   - Provides tailored exercise suggestions for each BMI category.
   - Includes beginner, intermediate, and advanced exercise options.

3. **Diet Suggestions**:
   - Offers diet tips and macronutrient balance recommendations based on BMI.
   - Includes practical advice for maintaining or achieving a healthy weight.

4. **User-Friendly Interface**:
   - Features a menu-driven system for easy navigation.
   - Validates user input to ensure accurate results.

---

## Files
### 1. `project.py`
This is the main Python script that contains all the logic for the BMI Calculator. It includes the following functions:
- **`calculate_bmi(weight, height)`**: Computes the BMI using the provided weight and height.
- **`classify_bmi(bmi)`**: Classifies the BMI into one of four categories.
- **`get_exercise_recommendation(category)`**: Returns exercise recommendations based on the BMI category.
- **`get_diet_suggestions(category)`**: Provides diet tips and macronutrient advice based on the BMI category.
- **`get_user_input()`**: Prompts the user for weight and height, with input validation.
- **`display_menu()`**: Displays a menu for the user to choose between BMI calculation, exercise recommendations, and diet suggestions.
- **`main()`**: The main function that runs the program and handles user interaction.

### 2. `test_project.py`
This file contains unit tests for the functions in `project.py`. It uses the `pytest` framework to ensure the code works as expected. The tests include:
- **`test_calculate_bmi()`**: Tests the BMI calculation function.
- **`test_classify_bmi()`**: Tests the BMI classification function.
- **`test_get_user_input()`**: Simulates user input to test the input function.

### 3. `requirements.txt`
This file lists the dependencies required to run the project. For this project, the only dependency is `pytest` for running the tests:

### 4. `README.md`
This file provides an overview of the project, its features, and instructions for running the program. It also documents design choices and explains the purpose of each file.

---

## Design Choices
### 1. **Modular Code Structure**
The program is divided into multiple functions, each responsible for a specific task. This modular approach makes the code:
- **Easier to read and maintain**: Each function has a clear purpose.
- **Reusable**: Functions like `calculate_bmi` and `classify_bmi` can be reused in other projects.
- **Testable**: Each function can be tested independently using `pytest`.

### 2. **Input Validation**
The `get_user_input` function ensures the user enters valid numeric values for weight and height. It also checks that the values are greater than zero. This prevents errors and ensures accurate BMI calculations.

### 3. **Exercise and Diet Recommendations**
The program uses dictionaries to store exercise and diet recommendations. This approach:
- **Simplifies data management**: All recommendations are stored in a structured format.
- **Makes it easy to update**: New recommendations can be added without changing the program logic.

### 4. **Menu-Driven Interface**
The `display_menu` function allows users to choose between BMI calculation, exercise recommendations, and diet suggestions. This makes the program interactive and user-friendly.

---

## How to Run the Program
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd project
   
   References:
   OpenAI. (2025). ChatGPT response to a question about [how to calculate MBI + CODING]. Retrieved March 2, 2025, from https://chat.openai.com
   Cleveland Clinic. (n.d.). Body mass index (BMI). Retrieved March 4, 2025, from https://my.clevelandclinic.org/health/articles/9464-body-mass-index-bmi
