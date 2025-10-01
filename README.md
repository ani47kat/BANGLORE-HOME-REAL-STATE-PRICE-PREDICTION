Project: Bangalore Home Price Prediction

Ye ek web-based application hai jo users ko Bangalore ke ghar ke estimated price ka idea deta hai. Isme user-friendly frontend aur Python Flask backend ka use kiya gaya hai.

Features:

Area Input: Users apne ghar ka square feet enter kar sakte hain.

BHK Selection: 1–5 BHK radio buttons ke through select kar sakte hain.

Bathroom Selection: 1–5 bathrooms select karne ka option.

Location Dropdown: Saari Bangalore locations dynamically backend se fetch hoti hain.

Price Estimation: “Estimate Price” button press karte hi machine learning model ke through predicted price show hota hai (in Lakh).

Technology Stack:

Frontend: HTML, CSS, JavaScript, jQuery

Backend: Python Flask

Machine Learning Model: Linear Regression (trained on Bangalore housing dataset)

AJAX: Server se asynchronous data fetch karne ke liye

How It Works:

User form fill karta hai → area, BHK, bathroom, location.

AJAX POST request backend me jati hai → trained model use karke estimated price calculate karta hai.

Result frontend me reload kiye bina show hota hai.

Locations dropdown backend se GET request ke through dynamically populate hota hai.

Purpose:

Quick Price Estimation: Real estate buyers aur sellers ke liye ghar ka approximate price jaanne ka fast tool.

User-Friendly: Simple interface aur live price estimation without page reload.

Dynamic & Scalable: Locations easily update ho sakti hain aur model retraining ke saath accurate predictions milti hain.
