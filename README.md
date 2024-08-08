
# House Price Prediction Web Application

This is a Flask web application that uses a machine learning model to predict the price of a house based on features that the user enters.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Implementation](#model-implementation)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

One project that shows how to include a machine learning model into a Flask web application is the House Price Prediction Web Application. The application allows users to input different house attributes and, using the trained model, provides an estimated house price.

## Features: 

- Offers an easy-to-use web interface for entering home characteristics
- Makes use of a machine learning model to forecast house price values depending on the features entered
- Displays the predicted house price to the user

## Installation

### requirements
- Python 3.x
- Flask
- scikit-learn
- jinja2
- python
- numpy


## usage
Using the Web Interface
1. Fill out the house feature form on the web page, providing details like the number of bedrooms,number of bathrooms, size of square feet, NO of floor etc.
2. Click the "Predict" button.
3. The application will display the predicted house price based on the provided features.

## Model Implementation

### Dataset
For this project, we used the dataset from Kaggle.

### Model Selection and Training
We implemented a LinearRegression is a machine learning algorithm used for predicting a continuous target variable based on linear relationships between features and target. The model was trained using the dataset and saved in the `models/train_model.pkl` file.


## Code Structure

### The project's code structure is as follows:
- `app.py`: The main Flask application file, handling routing and model integration.
- `templates/index.html`: The HTML template for the web interface.
- `static/css/main.css`: The CSS code for color, layout, and fonts, using properties and selectors for design control
- `train_model.pkl`: The serialized machine learning model.
- `house_data.csv`: The dataset used to train the machine learning model.
- `requirements.txt`: The list of Python dependencies for the project.
- `README.md`: The project's documentation, which you're currently reading.


![house1](https://github.com/user-attachments/assets/1d704bad-0265-4045-88bc-fc915fb70974)


![house2](https://github.com/user-attachments/assets/bf078db1-2b3f-474a-850d-8b88655c0bb2)


