# MP3-Group9
MP3 project for group 9. 

Contains:
- We are primarily analyzing the correlation of the running order of an entry from the Eurovision Song Contest and the final results for that country. We are also taking other factors into consideration like genre, countries etc.

Contributions:
- Tasks: MP3 notebook setup and data load/prep except for big-5 handling, additional modules plus init structure and setup, Mean-Shift clustering  - done by Nikolaj
- Linear regression and Naïve Bayes analysis of Eurovision finalists - done by Patrick
- Linear regression of semifinalists, README and questions - done by Jenny
- Classification of finalists via Decision Tree and Gradual Boosting Classifiers - done by David



README questions:

1. Which machine learning methods did you choose to analyze the impact of performance order on final rankings, and why?

- We chose to implement both Decision Tree and Gradient Boosting Classifiers for Eurovision prediction. Initially, we attempted to predict the exact placement (1-26), but later simplified to a binary classification task (Top 10 or Not). Gradient Boosting was selected because it creates an ensemble of trees that reduces overfitting and captures more complex patterns in the Eurovision voting data. The Decision Tree model provided a baseline for comparison and better interpretability.
- Multiple Linear Regression for training and testing a machine learning algorithm - to predict the results of an entry based on the running order, year, semifinal, total points and optionally jury points and televote points.

2. How accurate is your model in predicting final Eurovision rankings based on performance order? What quality measures did you use to evaluate the model’s effectiveness?

- Our binary classification model (Top 10 or Not) achieved approximately 67% accuracy, which represents a significant improvement over random guessing (50%). The model's metrics include:
Accuracy (0.67): The proportion of correct predictions (both true positives and true negatives)
Precision (0.65): When the model predicts a country will reach Top 10, it's correct 65% of the time
Recall (0.66): The model correctly identifies 66% of actual Top 10 finishers
F1 Score (0.65): The harmonic mean of precision and recall, providing a balanced measure of the model's performance

- Linear regression - semifinal: Since Eurovision results have a tendency to be quite unpredictable, we don't expect these predictions to be entirely accurate. But an variance score of 68% is pretty alright for a song contest with a small number of possible positions - in theory up until 26 - but ususally less than 20. That means of course that there is 32% of the result variance in the semifinals we don't account for. This can generally just stem from the upredictability of Eurovision results - like country-specific tendencies (diaspora voting, political voting, bloc-voting etc.), or just disrepancies between the juries and televotes. MAE = the predicted semifinal places are off by approximately 2.2 places - so a 10th place here could be between 7.8 and 12.2 in the actual result - which is pretty close.
MSE = A value of 7.04 indicates that, on average, the squared difference between predicted and actual places is 7.04, which in particular highlights the scale of this regression's errors due to the usage of squaring.
RMSE = A value of 2.65 means that, on average, the predicted semifinal place is off by around 2.65 places - which is also still reasonable.
Both R2 and the variance score are 0.68 - which means the model has covered 68% of the total variance in the semifinal results.

3. Which factors have the most significant influence on a song’s final ranking in the Eurovision Song Contest?

- The running order, genre, country other than the subjective opinions of the songs and staging itself.

4. How can the accuracy of your prediction model be further improved?

- Make some estimations around the probability of a jury favorite also having high televote scores and vice versa, and also the risk of an entry performing poorly in the other category.

5. Are certain performance positions (e.g., the “death slot” position 2) more likely to result in lower final rankings?
<img width="525" alt="image" src="https://github.com/user-attachments/assets/eee14ab3-a1b3-4de7-b9e0-a26c480c26f4" />

- Just from the semifinal linear regression itself we can tell that the boxplot for the 2nd position is placed in way higher placings (higher numbers) than the other positions, so this indicates that there is some truth to the theory of the death spot having a bigger risk of causing a worse result. 

6. Do jury votes and televotes differ in how they are influenced by performance order?
<img width="506" alt="image" src="https://github.com/user-attachments/assets/f7fb33a7-2c49-4f7a-860d-a6f711b2ec3e" />

- We haven't been able to answer this conclusively yet, but this correlation matrix indicates that the jury votes seems to align more with the final results than the televotes do. So they re probably influenced by the running order in different ways as well. 

7. How do viewership patterns, such as increasing audience size over the course of the show, affect the final results of songs performed later?

- In all our models the tendency seems to be that the later an act performs the better it tends to do - indicating possible recency bias.

8. Is there evidence of scoring bias based on factors like country, region, or performer gender?
<img width="931" alt="image" src="https://github.com/user-attachments/assets/f9e0b266-3f01-4a49-92a4-452de6286be0" />

- This graph indicates that an entry's country might influence how well it does. Other than political reasons, it can also just be because of some countries having more budget to work with, therefore making it easier to create and present a quality song and performance.


9. What were the key challenges in developing your analysis and prediction models for Eurovision?

- Dividing tasks, the dataset missing a few values in regards to the semifinal data creating a dilemma on whether to work around those and have to do lots of extra calculations to accomodate the missing values or remove those entries entirely - especially since it was only 2 entries. Also understanding how to calcualate and analyze the mean error models.
- It was difficult to make it work in the notebook, and to connect the notebook with streamlit
- It is difficult to know when you have collected enough data, as you can keep on adding more
