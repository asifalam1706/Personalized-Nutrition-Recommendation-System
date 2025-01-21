from flask import Flask, render_template, request
import pandas as pd
import numpy as np

# Create an instance of the Flask class
app = Flask(__name__)

# Load the dataset
raw = pd.read_csv("food.csv")

# Preprocess the dataset
raw['VegNovVeg'] = raw['VegNovVeg'].replace(' ', '0').astype(int)
raw = raw.drop(raw.tail(2).index)

# Function to calculate BMI and its category
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal"
    else:
        status = "Overweight"
    return bmi, status

# Function to filter food based on meal type
def filter_food_by_meal(data, meal_type):
    if meal_type == "Breakfast":
        return data[data['Breakfast'] == 1]
    elif meal_type == "Lunch":
        return data[data['Lunch'] == 1]
    elif meal_type == "Dinner":
        return data[data['Dinner'] == 1]

# Function to recommend diet based on BMI status
def recommend_diet(filtered_data, status):
    if status == "Underweight":
        return filtered_data[filtered_data['Calories'] > 200].head(3)
    elif status == "Overweight":
        return filtered_data[filtered_data['Calories'] < 150].head(3)
    else:  # Normal BMI
        return filtered_data[(filtered_data['Calories'] >= 150) & (filtered_data['Calories'] <= 250)].head(3)

# Flask Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user inputs
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])  # Get the age input

    # Calculate BMI
    bmi, status = calculate_bmi(weight, height)

    # Generate recommendations
    breakfast = recommend_diet(filter_food_by_meal(raw, "Breakfast"), status)
    lunch = recommend_diet(filter_food_by_meal(raw, "Lunch"), status)
    dinner = recommend_diet(filter_food_by_meal(raw, "Dinner"), status)

    # Convert recommendations to HTML tables
    breakfast_html = breakfast[['Food_items', 'Calories']].to_html(index=False, classes="table table-bordered")
    lunch_html = lunch[['Food_items', 'Calories']].to_html(index=False, classes="table table-bordered")
    dinner_html = dinner[['Food_items', 'Calories']].to_html(index=False, classes="table table-bordered")

    return render_template('index.html', bmi=f"{bmi:.2f}", status=status, age=age,
                           breakfast=breakfast_html, lunch=lunch_html, dinner=dinner_html)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
