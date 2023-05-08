# app.py
import streamlit as st
import random
import datetime

# List of 100 animals (replace with actual list)
animals = ['Animal 1', 'Animal 2', 'Animal 3', 'Animal 4', 'Animal 5'] * 20

# Function to generate a life recommendation in Japanese
def generate_recommendation(animal):
    # Replace with actual recommendations
    recommendations = {
        'Animal 1': '動物1に関連する人生の提案',
        'Animal 2': '動物2に関連する人生の提案',
        'Animal 3': '動物3に関連する人生の提案',
        'Animal 4': '動物4に関連する人生の提案',
        'Animal 5': '動物5に関連する人生の提案',
    }
    return recommendations[animal]

# Streamlit app
st.title('ChatGPT試用アプリ')
st.write('生年月日を入力してください。')

dob = st.date_input('生年月日', datetime.date(2000, 1, 1))

if st.button('結果を表示'):
    animal = random.choice(animals)
    recommendation = generate_recommendation(animal)
    st.write(f'あなたの動物: {animal}')
    st.write(f'あなたに関連する人生の提案: {recommendation}')
