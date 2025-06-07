# 🏏 IPL Victory Predictor

An interactive and visually appealing web application built with **Streamlit** to predict the winning probability of IPL teams during a match in real-time. Powered by a machine learning model trained on historical IPL data.

![Ipl-2021-ix7zwgff29ylomuf](https://github.com/user-attachments/assets/b964cace-11e7-451f-b825-fc4025751194)


---

## 🚀 Live Demo

🔗 **http://localhost:8501/**  


---

## 📸 Screenshot

![Screenshot (51)](https://github.com/user-attachments/assets/a2717dab-513d-4d1f-bee7-26002e66a2cb)


---

## 🔧 Features

✅ Select **Batting Team** and **Bowling Team**  
✅ Choose the **Venue**  
✅ Input live match data: **Target**, **Score**, **Overs**, **Wickets**  
✅ Predict win probability with a trained machine learning model  
✅ Beautiful IPL-themed background and intuitive interface  
✅ Handles edge cases and invalid inputs gracefully

---

## 📁 Project Structure

```bash
├── main.py                          # Streamlit app script
├── pipe.pkl                         # Trained ML pipeline (model)
├── Predictor.ipynb                  # Jupyter Notebook for training/preprocessing
├── deliveries.csv                   # Ball-by-ball delivery dataset
├── matches.csv                      # IPL match metadata
├── final_df.csv                     # Cleaned dataset used for training
├── Ipl-2021-ix7zwgff29ylomuf.jpg    # IPL background image
├── Screenshot (52).png              # UI screenshot
```

---

## 🧠 How It Works

1. **User Inputs** match conditions
2. **Features Computed**:
    - `runs_left = target - score`
    - `balls_left = 120 - (overs × 6)`
    - `wickets_remaining = 10 - wickets`
    - `crr = score / overs`
    - `rrr = runs_left / (balls_left / 6)`
3. These features are passed to a **trained machine learning model**
4. The model returns win probabilities for both teams

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ipl-victory-predictor.git
cd ipl-victory-predictor
pip install -r requirements.txt
streamlit run main.py
```

> Ensure all files (CSV, model, images) are in the same directory before running the app.

---

## 📊 Model Details

- **Input Features**:
  - Batting Team, Bowling Team, City
  - Runs Left, Balls Left, Wickets Remaining
  - Current Run Rate (CRR), Required Run Rate (RRR), Target Score

- **Model Type**: Logistic Regression (can be replaced with other classifiers)
- **Training Done In**: `Predictor.ipynb`

---

## 💻 Tech Stack

- Python
- Pandas, scikit-learn
- Streamlit (Frontend & Backend UI)
- Jupyter Notebook (for training/EDA)

---

## 🙌 Acknowledgments

- [Kaggle IPL Datasets](https://www.kaggle.com/datasets)
- Streamlit team for making ML app deployment so easy

---

## 📬 Contact

For questions, suggestions, or collaboration:
- GitHub: [@your-username](https://github.com/your-username)

---

## ⭐️ Support

If you like this project, give it a ⭐️ on GitHub!

---
