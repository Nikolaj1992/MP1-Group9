import streamlit as st

def show_problem_formulation():
    st.title("Eurovision Song Contest ML Project")
    st.header("📌 Tasks – Eurovision Song Contest Data Analysis and Prediction")

    st.subheader("1. Data Wrangling and Exploration")
    st.markdown("""
    - Load, clean, and explore available Eurovision Song Contest data (e.g., entries by year, country, song features, language, performance order, and final scores).  
    - Select and prepare the most relevant features of a song entry that will be useful for solving the following machine learning tasks.
    """)

    st.subheader("2. Supervised Machine Learning: Linear Regression")
    st.markdown("""
    - Train, test, and validate a machine learning model to predict the final score or ranking of a new Eurovision entry based on its characteristics.  
    - Apply appropriate evaluation measures (e.g., RMSE, R² score) to assess the quality of the model.
    """)

    st.subheader("3. Supervised Machine Learning: Classification")
    st.markdown("""
    - Train, test, and validate a classification model to predict whether a Eurovision entry will qualify for the Grand Final based on features such as country, genre, language, and performance slot.  
    - Evaluate the model using appropriate accuracy metrics (e.g., accuracy, precision, recall, F1-score).
    """)

    st.subheader("4. Unsupervised Machine Learning: Clustering")
    st.markdown("""
    - Apply a clustering algorithm (e.g., K-means) to segment Eurovision entries into groups of similarity (e.g., by musical style, performance patterns, or historical voting trends).  
    - Evaluate the clustering quality using a silhouette score and recommend the optimal number of clusters.
    """)

    st.subheader("5. Implementation of the Models in a Streamlit Application")
    st.markdown("""
    - Save the trained models to files for future use and deployment.  
    - Develop a user-friendly web application using Streamlit, allowing users to choose one of the three models and apply it to make predictions on new Eurovision entries.
    """)

    st.header("📄 README Questions for the Eurovision Song Contest ML Project")

    st.markdown("""
    **1. Which machine learning methods did you choose to apply in the application and why?**  
    Explain your choice of regression, classification, and clustering techniques, and how each is suitable for the specific Eurovision-related tasks.

    **2. How accurate is your solution for predicting Eurovision results? Explain the meaning of the quality measures.**  
    Discuss the performance of your regression and classification models using metrics such as R², RMSE, accuracy, precision, and F1-score.

    **3. Which are the most decisive factors influencing a country’s success in Eurovision? Why do certain entries perform better than others?**  
    Analyze key features like performance order, genre, or staging using feature importance or model interpretability tools.

    **4. What could be done for further improvement of the model accuracy?**  
    Suggest improvements such as hyperparameter tuning, feature engineering, or using more advanced ensemble models.

    **5. Which countries or types of songs are more likely to qualify for the final or place in the top 10?**  
    Analyze classification results for trends in musical style, language, or country.

    **6. Is there evidence of scoring bias related to country, region, or gender of performers?**  
    Explore whether certain demographics receive consistently higher or lower scores.

    **7. Do performance factors like time slot or song tempo influence the final results?**  
    Examine if early or late performances, or different tempos, affect results.

    **8. Does cultural or linguistic diversity of a song impact its success or audience reception?**  
    Analyze if multilingual or culturally unique entries have higher success rates.

    **9. What were the key challenges in the development of this project?**  
    Reflect on data collection, feature selection, model performance, or Streamlit implementation.
    """)

show_problem_formulation()