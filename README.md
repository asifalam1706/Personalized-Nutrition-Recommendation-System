# Personalized Nutrition Recommendation System
![Personalized Nutrition Recommendation System](https://github.com/user-attachments/assets/da18893d-b475-4655-a8f3-3894e7952715)

## 1. Introduction
In today’s fast-paced world, maintaining a healthy lifestyle is challenging due to a lack of personalized nutritional guidance. Each individual has unique dietary requirements influenced by their physical attributes (e.g., age, weight, height) and dietary preferences.
The Personalized Nutrition Recommendation System addresses this gap by calculating the user’s Body Mass Index (BMI) and providing food recommendations tailored to their BMI category. This project is designed to empower users to make informed dietary choices, promoting a balanced diet and healthier living.
## 2. Problem Statement
Maintaining a healthy lifestyle has become increasingly challenging due to:
* Lack of personalized nutritional advice.
* Generalized dietary plans that do not cater to individual needs.
The goal of this system is to:
1. Calculate the BMI of the user and classify it into three categories: Underweight, Normal, and Overweight.
2. Provide tailored food recommendations based on the user’s BMI category and dietary preferences.
This solution will empower users to achieve better health outcomes through informed dietary decisions.
## 3. Objectives
1. Build a user-friendly system that calculates BMI based on user inputs (age, weight, and height).
2. Categorize the user’s BMI into Underweight, Normal, or Overweight.
3. Provide personalized food recommendations for Breakfast, Lunch, and Dinner based on their BMI category:
   * Underweight: High-calorie food recommendations.
   *  Normal: Balanced-calorie food recommendations.
   *  Overweight: Low-calorie food recommendations.
  
## 4. Dataset
* Source: The dataset was collected from Kaggle.
* Structure:
   * Rows: 89 food items.
   * Columns: 16 (Food items, Breakfast, Lunch, Dinner, Veg/Non-Veg, Calories, Fats, Proteins, Iron, Calcium, Sodium, Potassium, Carbohydrates, Fiber, Vitamin D, Sugars).
## 5. Methodology
   * 1. BMI Calculation:
      
        * Formula used to calculate BMI.
        * Categories:
             * Underweight: BMI < 18.5
             * Normal: 18.5 ≤ BMI ≤ 24.9
             * Overweight: BMI > 24.9
  * 2. Recommendation System Logic:
        * User Input: Age, Weight, Height.
        * Steps:
             * Calculate BMI and identify the category.
             * Filter food items by meal type (Breakfast, Lunch, Dinner).
             * Recommend foods:
                  * Underweight: Calories > 200
                  * Normal: 150 ≤ Calories ≤ 250
                  * Overweight: Calories < 150
  * 3. Tools and Technologies:
       * Programming: Python
       * Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
       * Deployment: Flask for backend, HTML/CSS for frontend.
## 6. Machine Learning Models Attempted
  1. Decision Tree
  2. Random Forest
 3. Artificial Neural Network (ANN)
Findings:
    * All models resulted in accuracy scores of zero or less.
    * Potential reasons for poor performance:
         * Imbalanced Classes: Some food categories had very few entries.
         * Insufficient Data: Only 89 rows of data.
         * Misalignment: Dataset features may not align well with machine learning requirements.
## 7. User-Defined Function Approach
Due to the limitations of machine learning models, a rule-based system was implemented using user-defined functions. This approach leverages domain knowledge to provide accurate recommendations without relying on predictive models.

Advantages:
   * Direct and interpretable recommendations.
   * Effective for small datasets.

Avoids overfitting and generalization issues of ML models.

## 8. Deployment Using Flask
The system is deployed as a web-based application using Flask. Users input their weight and height to receive their BMI category and personalized food recommendations. The user interface is built with HTML, styled using CSS, and enhanced with Bootstrap for responsive design.

## 9. Results
   * BMI Classification:
     * Provides accurate categorization of BMI.
   * Food Recommendations:
     * Tailored recommendations for Breakfast, Lunch, and Dinner based on BMI.

![Screenshot 2025-01-02 195641](https://github.com/user-attachments/assets/79571c22-3b70-4412-adb7-cd3275bb0f49)
![Screenshot 2025-01-02 195723](https://github.com/user-attachments/assets/f5bd6556-c880-461a-839b-e0ce5e1027af)

## 10. Conclusion
Despite initial attempts to use machine learning models like Decision Tree, Random Forest, and ANN, all models failed to perform due to data limitations. To address this, a rule-based recommendation system was implemented using user-defined functions. This approach ensures accurate and meaningful recommendations by leveraging domain knowledge and the characteristics of the dataset.
The project demonstrates the importance of aligning the methodology with the problem's requirements and highlights the potential of personalized nutrition systems to promote healthier lifestyles.

## 11. References
  * Kaggle Dataset: https://www.kaggle.com/
  * Flask Documentation: Flask Framework
  * BMI Reference: https://www.who.int/


  
