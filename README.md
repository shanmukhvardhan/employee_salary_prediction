# 💼 Employee Salary Prediction App

## 📊 Overview
The **Employee Salary Prediction App** is a modern, interactive web tool built with **Streamlit** that estimates employee salaries based on demographic and professional attributes. Powered by a machine learning pipeline developed using **scikit-learn**, this app provides both individual predictions and batch salary estimations via CSV uploads.

It's built to assist **HR professionals**, **recruiters**, and **data analysts** in making quick, informed salary estimates during hiring, reviews, or workforce planning.

## 🌟 Features
- 🖥️ **User-Friendly Interface:** Clean layout with interactive inputs.
- ⚡ **Real-time Predictions:** Predict salaries instantly based on form inputs.
- 📂 **Batch Processing:** Upload a CSV file to get multiple predictions at once.
- ☁️ **Cloud Hosted:** Deployed live via Streamlit Cloud.
- 🔒 **Controlled Environment:** Fixed Python and scikit-learn versions for model stability.

## 🔢 Input Features
| Feature             | Description                                         |
|---------------------|-----------------------------------------------------|
| Age                 | Age in years                                        |
| Years of Experience | Total years of professional experience              |
| Education Level     | Bachelor / Master / PhD                             |
| Department          | E.g., Sales, Engineering, HR, Finance, etc.         |
| Job Title           | E.g., Engineer, Analyst, Intern, Manager, Executive |
| Gender              | Male, Female                                        |
| Location            | E.g., Austin, New York, Chicago                     |


### 🧰 Prerequisites
- Python 3.10+
- pip or conda


## 🌐 Deployed App
✅ You can try the app live here:  
👉 https://employeesalaryprediction-shanmukh-vardhan.streamlit.app/

## 🧠 Model Details
- Model File: `final_salary_model.pkl`
- ML Framework: `scikit-learn`
- Saved using version: `1.5.1`
- Python Version: `3.10`
- Pipeline uses preprocessing with `ColumnTransformer` and a regression model.


## 📄 Files Included
- `app.py` – Streamlit app source
- `requirements.txt` – Required Python packages
- `final_salary_model.pkl` – Trained regression model
- `logo.png` – Optional branding/logo


## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more info.

## 👤 Author
**Shanmukh Vardhan**  
📫 shanmukhvardhan1663@gmail.com.com  
🔗 https://github.com/shanmukhvardhan




