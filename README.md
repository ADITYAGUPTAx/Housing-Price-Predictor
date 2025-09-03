# Housing Price Predictor

A machine learning powered web app that predicts real estate prices in Bangalore based on location, square footage, number of bedrooms (BHK), and bathrooms.

---

## Why This Matters  
Housing affordability and transparency are big challenges in fast-growing cities like Bangalore. This tool helps users including buyers, sellers, and agents get data-driven pricing estimates instantly, bringing clarity and confidence to decision-making.

---

## Live Demo  
Try it here: [Housing Price Predictor on Render](https://housing-price-predictor-tlay.onrender.com)  
*(Note: Free hosting may take up to a minute to load.)*

---

## Dataset and Features  
The model is trained on real Bangalore housing market data.  

**Features used for prediction:**  
- Location (neighborhood, one-hot encoded)  
- Square Footage (size of the property in sq ft)  
- Bedrooms (BHK)  
- Bathrooms  

---

## Modeling Approach  

1. **Data Processing**  
   - Removed missing values and outliers  
   - Scaled numerical features  
   - One-hot encoded categorical variables such as location  

2. **Model Training**  
   - Evaluated multiple models: Linear Regression, Decision Tree, Random Forest, Gradient Boosting  
   - Selected Linear Regression for its strong performance and interpretability  

3. **Evaluation**  
   - Metrics used: RMSE and R²  
   - The final model achieved reliable performance on the test dataset, suitable for practical use  

---

## Tech Stack  

- **Backend**: Python, Flask, pickle for model serialization  
- **Frontend**: HTML, CSS (Bootstrap optional)  
- **ML Libraries**: scikit-learn, pandas, numpy  
- **Hosting**: Render.com  
- **Dev Tools**: GitHub for version control  

---

## How to Use  

1. Clone the Repository  
   ```bash
   git clone https://github.com/ADITYAGUPTAx/Housing-Price-Predictor.git
   cd Housing-Price-Predictor
Install Dependencies

pip install -r requirements.txt


Run Locally

python server.py


Open your browser at http://localhost:5000
Enter housing details and get an instant price prediction
