## Customer Churn Prediction Web Application

This is a Streamlit-based web application that predicts customer churn based on user inputs. It uses a pre-trained machine learning model to provide predictions on whether a customer is likely to churn or stay based on their demographic, financial, and interaction data.

## Features

- Age, Job, Marital Status, Housing Loan, Personal Loan, Contact Type, Outcome of Previous Campaign: User input fields.
- Model Prediction: Based on input values, the model predicts whether the customer is likely to churn.
- Interactive UI: Built with Streamlit, allowing easy interaction and quick results.
  
**Installation and Usage**

### Prerequisites

- Python 3.x
- `pip` or `conda` for package management

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-churn-prediction-app.git
   cd customer-churn-prediction-app
   ```

2. Ensure you have the pre-trained model file (`finalized_model.sav`) in the root directory of the project. The model should be a serialized machine learning model, trained on the appropriate dataset for predicting churn.

3. Run the application:
   ```bash
   streamlit run web_application.py
   ```
45. Open the local URL provided by Streamlit in your web browser to access the application.

## Input Fields

- **Age**: Numeric input for the customer's age.
- **Job**: Dropdown menu with job categories.
- **Marital Status**: Dropdown menu for selecting marital status.
- **Housing Loan**: Dropdown to indicate whether the customer has a housing loan.
- **Personal Loan**: Dropdown to indicate whether the customer has a personal loan.
- **Contact Type**: Dropdown menu to choose the type of contact (e.g., cellular, telephone).
- **Outcome of Previous Campaign**: Dropdown to select the outcome of the previous marketing campaign (failure, nonexistent, success).
- **Consumer Confidence Index**: Numeric input field.
- **Euribor 3-Month Rate**: Numeric input field.
- **Number of Employees**: Numeric input field to specify the number of employees.

## Prediction

The application predicts whether a customer will churn or not based on the input data. It uses a machine learning model loaded from a serialized file (`finalized_model.sav`).

- If the prediction is "Yes", it means the customer is likely to churn.
- If the prediction is "No", it means the customer is likely to stay.

## Model

- The machine learning model is trained on customer data and is saved as a serialized file (`finalized_model.sav`).
- The model expects the following features for prediction:
  - Age, Job, Marital Status, Housing Loan, Personal Loan, Contact Type, Outcome of Previous Campaign, Consumer Confidence Index, Euribor 3-Month Rate, Number of Employees.
- The features are pre-processed using `ColumnTransformer` that applies standard scaling to numerical features and ordinal encoding to categorical features.

## Dependencies

The following Python libraries are required to run this application:

- **Streamlit**: For building the web interface.
- **Pandas**: For handling data.
- **NumPy**: For numerical operations.
- **Pickle**: For loading the pre-trained model.
- **scikit-learn**: For pre-processing data and performing predictions.

## Repository Structure

```
.
├── web_application.py       # The main application file
├── finalized_model.sav      # The pre-trained model file
└── .gitignore               # Git ignore file
```

## Screenshots

![image](https://github.com/user-attachments/assets/8318bee6-7f89-4691-bcf4-d5a40e7eccf8)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
