import streamlit as st
import datetime

# Define the 10 animals and their associated life sayings in Japanese
animals = {
    "鼠": "一寸先は闇",
    "牛": "一日千秋",
    "虎": "虎穴に入らずんば虎子を得ず",
    "兎": "走る狗に肉を与えるな",
    "龍": "風水の神様",
    "蛇": "蛇の道は蛇",
    "馬": "馬の耳に念仏",
    "羊": "羊頭狗肉",
    "猿": "猿木から落ちる",
    "鶏": "鶏口となるも牛後となるな"
}

# Define a function to calculate the animal based on the date of birth
def calculate_animal(date_of_birth):
    year = date_of_birth.year
    animal_index = (year - 4) % 12
    animal = list(animals.keys())[animal_index]
    return animal

# Define the Streamlit app
def app():
    st.title("Animal and Life Proverb Calculator")
    st.write("Enter your date of birth to find out your animal and associated life proverb in Japanese.")
    date_of_birth = st.date_input("Date of Birth")
    if date_of_birth:
        animal = calculate_animal(date_of_birth)
        life_saying = animals[animal]
        st.write(f"Your animal is {animal} and your associated life proverb is '{life_saying}'.")

# Call the app function to run the Streamlit app
app()
