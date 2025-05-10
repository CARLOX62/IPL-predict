import base64
import streamlit as st
import pickle

import pandas as pd
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("C:/Users/HP/Desktop/CODES/ML_Projects/IPL Win Probability Predictor/Ipl-2021-ix7zwgff29ylomuf.jpg")
# data:image/png;base64,{img}
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
width: 100%;
height:100%;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
teams =['--- select ---',
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Kolkata Knight Riders',
        'Royal Challengers Bangalore',
        'Kings XI Punjab',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals']
cities =['Bangalore', 'Hyderabad', 'Kolkata', 'Mumbai', 'Visakhapatnam',
       'Indore', 'Durban', 'Chandigarh', 'Delhi', 'Dharamsala',
       'Ahmedabad', 'Chennai', 'Ranchi', 'Nagpur', 'Mohali', 'Pune',
       'Bengaluru', 'Jaipur', 'Port Elizabeth', 'Centurion', 'Raipur',
       'Sharjah', 'Cuttack', 'Johannesburg', 'Cape Town', 'East London',
       'Abu Dhabi', 'Kimberley', 'Bloemfontein']

try:
    with open('pipe.pkl', 'rb') as f:
        pipe = pickle.load(f)
except FileNotFoundError:
    st.error("Model file (pipe.pkl) not found. Please ensure it's in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    # **IPL VICTORY PREDICTOR**            
""")
# st.title("IPL Victory Predictor")

col1, col2 = st.columns(2)

with col1:
   
   batting_team =  st.selectbox('Select Batting Team',teams)

with col2:
    if batting_team == '--- select ---':
        bowling_team = st.selectbox('Select Bowling Team', teams)
    else:
        filtered_teams = [team for team in teams if team != batting_team]
        bowling_team = st.selectbox('Select Bowling Team', filtered_teams)

seleted_city = st.selectbox('Select Venue',cities)

target = st.number_input('Target')

col1,col2,col3 = st.columns(3)

with col1:
    score = st.number_input('Score')
with col2:
    overs = st.number_input("Over Completed")
with col3:
    wickets = st.number_input("Wickets down")

if st.button('Predict Winning Probability'):
    try:
        if wickets > 10 or overs > 20:
            st.error("Wickets can't be more than 10 and overs can't exceed 20.")
        else:
            runs_left = target - score
            balls_left = 120 - (overs * 6)
            wickets_remaining = 10 - wickets
            crr = score / overs if overs > 0 else 0
            rrr = runs_left / (balls_left / 6) if balls_left > 0 else 0

            input_data = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [seleted_city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets': [wickets_remaining],
                'total_runs_x': [target],
                'crr': [crr],
                'rrr': [rrr]
            })

            with st.spinner("Predicting..."):
                result = pipe.predict_proba(input_data)

            loss = result[0][0]
            win = result[0][1]
            st.success("Prediction complete ✅")
            st.header(f"{batting_team} = {round(win*100)}%")
            st.header(f"{bowling_team} = {round(loss*100)}%")

    except Exception as e:
        st.error(f"Some error occurred: {str(e)}")
