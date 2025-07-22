import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Employee Salary Estimator", page_icon="💵", layout="centered")

# Header and Description
st.markdown("<style>h1{color:#00aaff;}</style>", unsafe_allow_html=True)
st.title("💵 Employee Salary Estimator")
st.subheader("A modern, AI-powered salary forecast app")

# Sidebar with user instructions
with st.sidebar:
    st.image("logo.png", width=140)  # (Replace with your logo)
    st.markdown("### Welcome!")
    st.info("Fill in details to estimate your predicted salary. Try different combinations or upload a CSV for batch predictions.")

# Main form input
with st.form("prediction_form"):
    st.markdown("#### Enter Employee Details")
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 18, 70, 30, help="Enter the employee's age")
        exp = st.slider("Years of Experience", 0, 50, 5, help="Total professional experience")
        education = st.selectbox("Education", ["Bachelor", "Master", "PhD"])
        gender = st.radio("Gender", ["Male", "Female"])
    with col2:
        department = st.selectbox("Department", ["Sales", "Engineering", "HR", "Finance", "Product", "Marketing"])
        job_title = st.selectbox("Job Title", ["Manager", "Engineer", "Analyst", "Intern", "Executive"])
        location = st.selectbox("Location", ["Austin", "Seattle", "Chicago", "New York", "San Francisco"])

    submitted = st.form_submit_button("🔮 Predict Salary")
    if submitted:
        input_df = pd.DataFrame({
            "Age": [age],
            "Experience_Years": [exp],
            "Education_Level": [education],
            "Department": [department],
            "Job_Title": [job_title],
            "Gender": [gender],
            "Location": [location]
        })
        model = joblib.load("final_salary_model.pkl")
        predicted_salary = model.predict(input_df)[0]
        with st.spinner("Calculating..."):
            st.success(f"🏆 Estimated Monthly Salary: ${predicted_salary:,.0f}")

# Batch prediction section
st.markdown("---")
st.markdown("#### 📂 Batch Salary Predictions")
uploaded_file = st.file_uploader("Upload a CSV file with employee data for bulk predictions", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    model = joblib.load("final_salary_model.pkl")
    preds = model.predict(data)
    data['PredictedSalary'] = preds
    st.dataframe(data.head())
    st.download_button("Download Results as CSV", data.to_csv(index=False).encode('utf-8'), file_name="predicted_salaries.csv")

# (Optional) Add feature importance, model confidence, or contact/about sections for professional enhancements!
