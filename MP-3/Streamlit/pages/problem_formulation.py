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
    - Train, test, and validate a classification model to predict whether a Eurovision entry will be in Top 10 in the Grand Final based on features performance slot and votes.  
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
    1. **Which machine learning methods did you choose to analyze the impact of performance order on final rankings, and why?**
    - We chose to implement both **Decision Tree** and **Gradient Boosting Classifiers** for Eurovision prediction. Initially, we attempted to predict the exact placement (1-26), but later simplified to a binary classification task (Top 10 or Not). **Gradient Boosting** was selected because it creates an ensemble of trees that reduces overfitting and captures more complex patterns in the Eurovision voting data. The **Decision Tree model** provided a baseline for comparison and better interpretability. 
    - **Multiple Linear Regression** for training and testing a machine learning algorithm - to predict the results of an entry based on the running order, year, semifinal, total points and optionally jury points and televote points.

    2. **How accurate is your model in predicting final Eurovision rankings based on performance order? What quality measures did you use to evaluate the model’s effectiveness?**
    - Our binary classification model (Top 10 or Not) achieved approximately **67% accuracy**, which represents a significant improvement over random guessing (50%). The model's metrics include:
    - **Accuracy (0.67)**: The proportion of correct predictions (both true positives and true negatives)
    - **Precision (0.65)**: When the model predicts a country will reach Top 10, it's correct 65% of the time
    - **Recall (0.66)**: The model correctly identifies 66% of actual Top 10 finishers
    - **F1 Score (0.65)**: The harmonic mean of precision and recall, providing a balanced measure of the model's performance
    - **Linear regression - semifinal**: Since Eurovision results are quite unpredictable, we don't expect these predictions to be entirely accurate. But a variance score of **68%** is pretty good for a song contest with a small number of possible positions. 
    - **MAE** = The predicted semifinal places are off by approximately **2.2 places**.
    - **MSE** = A value of **7.04** indicates that, on average, the squared difference between predicted and actual places is **7.04**.
    - **RMSE** = A value of **2.65** means the predicted semifinal place is off by around **2.65 places**.

    3. **Which factors have the most significant influence on a song’s final ranking in the Eurovision Song Contest?**
    - The **running order**, **genre**, **country**, and other subjective opinions on the songs and their staging itself.

    4. **How can the accuracy of your prediction model be further improved?**
    - Make some estimations around the probability of a jury favorite also having high televote scores and vice versa, and also the risk of an entry performing poorly in the other category.

    5. **Are certain performance positions (e.g., the “death slot” position 2) more likely to result in lower final rankings?**
    """)
    st.image("https://github.com/user-attachments/assets/eee14ab3-a1b3-4de7-b9e0-a26c480c26f4", width=525)

    st.markdown("""
    - Just from the semifinal linear regression itself, we can tell that the boxplot for the 2nd position is placed in much higher placements (higher numbers) than the other positions. This indicates that there is some truth to the theory of the **death spot** having a bigger risk of causing a worse result.
    """)

    st.markdown("""
    6. **Do jury votes and televotes differ in how they are influenced by performance order?**
    """)
    st.image("https://github.com/user-attachments/assets/f7fb33a7-2c49-4f7a-860d-a6f711b2ec3e", width=506)

    st.markdown("""
    - We haven't been able to answer this conclusively yet, but this correlation matrix indicates that the **jury votes** seem to align more with the final results than the **televotes** do. They are probably influenced by the running order in different ways as well.
    """)

    st.markdown("""
    7. **How do viewership patterns, such as increasing audience size over the course of the show, affect the final results of songs performed later?**
    - In all our models, the tendency seems to be that the later an act performs, the better it tends to do — indicating possible **recency bias**.
    
    8. **Is there evidence of scoring bias based on factors like country, region, or performer gender?**
    """)
    st.image("https://github.com/user-attachments/assets/f9e0b266-3f01-4a49-92a4-452de6286be0", width=931)

    st.markdown("""
    - This graph indicates that an entry’s **country** might influence how well it does. Apart from political reasons, it can also be due to some countries having larger budgets, making it easier to create and present a high-quality song and performance.
    """)

    st.markdown("""
    9. **What were the key challenges in developing your analysis and prediction models for Eurovision?**
    - Dividing tasks, the dataset missing a few values in regard to the semifinal data, creating a dilemma on whether to work around those and perform extra calculations to accommodate the missing values or remove those entries entirely (which only affected 2 entries).
    - It was difficult to make it work in the notebook, and to connect the notebook with **Streamlit**.
    - It is difficult to know when to stop collecting data, as you can keep on adding more.
    """)

# Call the function to display the content
show_problem_formulation()
