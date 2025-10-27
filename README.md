# 🏡 Bangalore Home Price Prediction

Welcome to the **Bangalore Home Price Prediction** project! 🎉  
This is a **web-based application** that predicts the price of houses in Bangalore using a **machine learning model** and a **user-friendly web interface**.  

---

## ✨ Features

- **📏 Area Input:** Enter the total square footage of the house.  
- **🛏 BHK Selection:** Choose the number of bedrooms (1–5) via radio buttons.  
- **🛁 Bathroom Selection:** Select the number of bathrooms (1–5).  
- **📍 Location Dropdown:** Dynamically fetched list of all Bangalore locations.  
- **💰 Price Estimation:** Click **“Estimate Price”** to get the predicted price in **Lakhs**.  

---

## 🛠 Technology Stack

- **Frontend:** HTML, CSS, JavaScript, jQuery  
- **Backend:** Python Flask  
- **Machine Learning Model:** Linear Regression (trained on Bangalore housing dataset)  
- **AJAX:** Enables smooth, asynchronous communication between frontend and backend  

---

## ⚙️ How It Works

1. The user fills in the form: **area, BHK, bathrooms, and location**.  
2. An **AJAX POST request** is sent to the backend.  
3. The **model predicts the house price**.  
4. The **result is displayed instantly** on the frontend without reloading the page.  
5. The **location dropdown** is dynamically populated via an AJAX GET request.  

---

## 🎯 Purpose

- **Quick Price Estimation:** Helps buyers and sellers get a fast idea of house prices.  
- **User-Friendly:** Clean and interactive interface with live predictions.  
- **Dynamic & Scalable:** Locations can be updated easily, and the ML model can be retrained to improve accuracy.  

---

## 📸 Screenshot 

![Screenshot](https://github.com/ani47kat/ani47kat.github.io/blob/main/screenshot.png)  

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bangalore-home-price-prediction.git
