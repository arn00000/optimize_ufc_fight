import os
import streamlit as st
import streamlit.components.v1 as components
import pickle

with open('random_forest_model.h5', 'rb') as file:
    model = pickle.load(file)

def predict_popu(R_KD, B_KD, R_SUB_ATT, B_SUB_ATT, R_CTRL,
       B_CTRL, R_LANDED_HEAD, B_LANDED_HEAD, R_LANDED_GROUND,
       B_LANDED_GROUND,R_LANDED_BODY,B_LANDED_BODY,R_LANDED_LEG,B_LANDED_LEG,
    R_LANDED_CLINCH,B_LANDED_CLINCH,
       title_bout,B_Stance,R_Stance,R_SIG_TD,B_SIG_TD,B_DISTANCE,R_DISTANCE):
    
    prediction = model.predict([[R_KD, B_KD, R_SUB_ATT, B_SUB_ATT, R_CTRL,
       B_CTRL, R_LANDED_HEAD, B_LANDED_HEAD, R_LANDED_GROUND,
       B_LANDED_GROUND,R_LANDED_BODY,B_LANDED_BODY,R_LANDED_LEG,B_LANDED_LEG,
    R_LANDED_CLINCH,B_LANDED_CLINCH,
       title_bout,B_Stance,R_Stance,R_SIG_TD,B_SIG_TD,B_DISTANCE,R_DISTANCE]])
    return prediction[0]

def main():
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UFC_Logo.svg/330px-UFC_Logo.svg.png',width=300)
    st.title("Optimize UFC fights for Betting")
    st.text('Enter both figther previous fight stats to predict their upcoming fight winner.')
    title_bout = st.selectbox(
            'Is this Title Bout',
            (False, True))

    col1, col2 = st.columns(2)
    with col1:
        Red = st.text_input('Red corner figther name', 'Red Corner')
    with col2:
        Blue = st.text_input('Blue corner figther name', 'Blue Corner')
    with col1:
        R_Stance = st.selectbox(
            'Select Red fight stance',
            ('Orthodox', 'Southpaw', 'Switch'))
    with col2:
        B_Stance = st.selectbox(
            'Select Blue fight stance',
            ('Orthodox', 'Southpaw', 'Switch'))
    with col1:
        R_KD = st.number_input("R_How many KO in last fight?",min_value=0, step=1)
    with col2:
        B_KD = st.number_input("B_How many KO in last fight?",min_value=0, step=1)
    with col1: 
        R_CTRL = st.number_input('R_Control time by second',min_value=0, step=1)
    with col2:
        B_CTRL = st.number_input('B_Control time by second',min_value=0, step=1)
    with col1:
        R_SUB_ATT = st.slider('R_Submission attemp', 0, 10)
    with col2:
        B_SUB_ATT = st.slider('B_Submission attemp', 0, 10)
    with col1:
        R_SIG_TD = st.slider('R_Take down attemp', 0, 20)
    with col2:
        B_SIG_TD = st.slider('B_Take down attemp', 0, 20)
    with col1:
        R_LANDED_HEAD = st.slider('R_Significant strike on head', 0, 100)
    with col2:
        B_LANDED_HEAD = st.slider('B_Significant strike on head', 0, 100)
    with col1:
        R_LANDED_BODY = st.slider('R_Significant strike on body', 0, 100)
    with col2:
        B_LANDED_BODY = st.slider('B_Significant strike on body', 0, 100)
    with col1:
        R_LANDED_LEG = st.slider('R_Significant strike on leg', 0, 100)
    with col2:
        B_LANDED_LEG = st.slider('B_Significant strike on leg', 0, 100)
    with col1:
        R_DISTANCE = st.slider('R_DISTANCE', 0, 150)
    with col2:
        B_DISTANCE = st.slider('B_DISTANCE', 0, 150)
    with col1:
        R_LANDED_CLINCH = st.slider('R_Clinch attemp', 0, 50)
    with col2:
        B_LANDED_CLINCH = st.slider('B_Clinch attemp', 0, 50)
    with col1:
        R_LANDED_GROUND = st.slider('R_Ground and Pound', 0, 100)
    with col2:
        B_LANDED_GROUND = st.slider('B_Ground and Pound', 0, 100)
  
        
    result=''
    st.text("Prediction accuracy up to 87%")
    if st.button('Predict'):
        if B_Stance == 'Orthodox':
            B_Stance = 1
        elif B_Stance == 'Southpaw':
            B_Stance = 3
        else:
            B_Stance = 4
        if R_Stance == 'Orthodox':
            R_Stance = 1
        elif R_Stance == 'Southpaw':
            R_Stance = 3
        else:
            R_Stance = 4
            
        if title_bout == True:
            title_bout = 1
        elif title_bout == False:
            title_bout = 0
        result = predict_popu(R_KD, B_KD,R_SUB_ATT, B_SUB_ATT, R_CTRL,
           B_CTRL, R_LANDED_HEAD, B_LANDED_HEAD, R_LANDED_GROUND,
           B_LANDED_GROUND,R_LANDED_BODY,B_LANDED_BODY,R_LANDED_LEG,B_LANDED_LEG,
            R_LANDED_CLINCH,B_LANDED_CLINCH,
           title_bout,B_Stance,R_Stance,R_SIG_TD,B_SIG_TD,B_DISTANCE,R_DISTANCE)
        if result == 2:
            result = 'The winner is ' + Red
        elif result == 0:
            result = 'The winner is ' + Blue
        elif result == 1:
            result = 'Is a Draw'
        st.success(format(result))
    
if __name__ == '__main__':
    main()
