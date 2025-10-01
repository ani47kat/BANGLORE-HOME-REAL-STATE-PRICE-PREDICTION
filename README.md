Project: Bangalore Home Price Prediction

This is a web-based application that provides users with an estimated price of houses in Bangalore. The project combines a user-friendly frontend with a Python Flask backend powered by a machine learning model.

Features:

Area Input: Users can enter the total square footage of the house.

BHK Selection: Users can select the number of bedrooms (1–5) via radio buttons.

Bathroom Selection: Users can select the number of bathrooms (1–5).

Location Dropdown: All Bangalore locations are dynamically fetched from the backend.

Price Estimation: Clicking the “Estimate Price” button calculates the predicted house price (in Lakh) using a trained machine learning model.

Technology Stack:

Frontend: HTML, CSS, JavaScript, jQuery

Backend: Python Flask

Machine Learning Model: Linear Regression (trained on Bangalore housing dataset)

AJAX: Asynchronous communication between frontend and backend

How It Works:

The user fills in the form → area, BHK, bathrooms, and location.

An AJAX POST request is sent to the backend → the model predicts the estimated price.

The result is displayed on the frontend without reloading the page.

The location dropdown is dynamically populated via an AJAX GET request to the backend.

Purpose:

Quick Price Estimation: Helps real estate buyers and sellers get a quick idea of house prices.

User-Friendly: Clean interface with live price prediction.

Dynamic & Scalable: Locations can easily be updated, and the model can be retrained to improve accuracy.
