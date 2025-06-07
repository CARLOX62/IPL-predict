```markdown
# 🏏 IPL Victory Predictor

An interactive and visually stunning web application built using **Streamlit** to predict the winning probability of IPL teams during a match in real time. It uses a trained ML model (pipeline) and historical data to provide accurate predictions based on match progress.

![IPL Banner](Ipl-2021-ix7zwgff29ylomuf.jpg)

## 🚀 Live Demo

🔗 **http://localhost:8501/**  


---

## 📸 Screenshot

![Screenshot (51)](https://github.com/user-attachments/assets/0c3505c0-78f3-438d-a113-801bdbaa5617)


---

## 🔧 Features

- Select **Batting** and **Bowling** teams from official IPL lineups.
- Choose match **venue**, enter **target**, **score**, **overs completed**, and **wickets down**.
- Instant prediction of **win probability** using a machine learning model.
- Visually appealing interface with dynamic background based on IPL visuals.
- Error-handling for invalid inputs and missing files.

---

## 📁 Project Structure

```bash
├── Predictor.ipynb                    # Jupyter Notebook for model training/testing
├── main.py                            # Streamlit web app
├── pipe.pkl                           # Trained pipeline (ML model)
├── deliveries.csv                     # Raw IPL delivery-level data
├── final_df.csv                       # Processed feature dataset
├── matches.csv                        # IPL match-level data
├── Ipl-2021-ix7zwgff29ylomuf.jpg      # Background IPL image
├── Screenshot (52).png                # UI Screenshot
```

---

## 🧠 How It Works

- **User Input:** Match context (teams, score, overs, etc.)
- **Feature Engineering:** Calculates:
  - `runs_left = target - score`
  - `balls_left = 120 - (overs * 6)`
  - `crr = score / overs`
  - `rrr = runs_left / (balls_left / 6)`
- **Model Inference:** A trained pipeline (`pipe.pkl`) predicts win probability.
- **Output:** Displays probability for both teams visually.

---

## 📦 Installation

```bash
git clone https://github.com/CARLOX62/IPL-predict.git
cd IPL-predict
pip install -r requirements.txt
streamlit run main.py
```

> Ensure `pipe.pkl`, image, and all CSV files are in the same directory as `main.py`.

---

## 📊 Model & Dataset

- Model trained on IPL match data using classifiers (like Logistic Regression).
- Important Features:
  - Team info, venue, match status
  - Engineered stats (runs_left, crr, rrr, etc.)
- Datasets:
  - `deliveries.csv` – Ball-level details
  - `matches.csv` – Match metadata
  - `final_df.csv` – Processed features

---

## 🌐 Tech Stack

- **Python**
- **Pandas**, **NumPy**, **scikit-learn**
- **Streamlit** for the web interface

---

## 🙌 Acknowledgments

Thanks to Streamlit, IPL open dataset providers, and ML communities that inspired this app.

---

## 📬 Contact

Raise an [issue](https://github.com/CARLOX62/IPL-predict/issues) or connect via GitHub for improvements or questions.

---

⭐️ *If you like this project, give it a star!*
```
