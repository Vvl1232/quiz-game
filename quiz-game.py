#=================================================verification data=============================================================
data = [
    ("Color of the sky?", "Blue"),
    ("Shape of the Earth?", "Round"),
    ("Color of grass?", "Green"),
    ("Taste of salt?", "Salty"),
    ("Sound of thunder?", "Loud"),
    ("Touch of fire?", "Hot"),
    ("State of water at 0°C?", "Ice"),
    ("Position of the sun at noon?", "Top"),
    ("Color of a banana?", "Yellow"),
    ("Direction of sunrise?", "East"),
    ("Color of the ocean?", "Blue"),
    ("Shape of a wheel?", "Round"),
    ("Color of an apple?", "Red"),
    ("Taste of sugar?", "Sweet"),
    ("Sound of rain?", "Pitter-patter"),
    ("Touch of ice?", "Cold"),
    ("State of water at 100°C?", "Steam"),
    ("Position of the moon at night?", "Sky"),
    ("Color of an orange?", "Orange"),
    ("Direction of sunset?", "West"),
    ("Color of a leaf?", "Green"),
    ("Shape of a square?", "Square"),
    ("Color of snow?", "White"),
    ("Taste of lemon?", "Sour"),
    ("Sound of a bell?", "Ring"),
    ("Touch of sandpaper?", "Rough"),
    ("State of water at room temperature?", "Liquid"),
    ("Position of stars?", "Sky"),
    ("Color of coal?", "Black"),
    ("Direction of a compass needle?", "North"),
    ("Color of a rose?", "Red"),
    ("Shape of a triangle?", "Triangular"),
    ("Color of honey?", "Gold"),
    ("Taste of chocolate?", "Sweet"),
    ("Sound of a car horn?", "Honk"),
    ("Touch of a feather?", "Soft"),
    ("State of butter in the fridge?", "Solid"),
    ("Position of clouds?", "Sky"),
    ("Color of a flamingo?", "Pink"),
    ("Direction of river flow?", "Downstream"),
    ("Color of a frog?", "Green"),
    ("Shape of a rectangle?", "Rectangular"),
    ("Color of the moon?", "White"),
    ("Taste of vinegar?", "Sour"),
    ("Sound of a clock?", "Tick"),
    ("Touch of velvet?", "Soft"),
    ("State of iron at room temperature?", "Solid"),
    ("Position of the sun at sunset?", "Horizon"),
    ("Color of an egg yolk?", "Yellow"),
    ("Direction of a bird's flight?", "Up"),
    ("Color of a carrot?", "Orange"),
    ("Shape of a diamond?", "Diamond"),
    ("Color of an octopus?", "Purple"),
    ("Taste of saltwater?", "Salty"),
    ("Sound of footsteps?", "Step"),
    ("Touch of silk?", "Smooth"),
    ("State of steam?", "Gas"),
    ("Position of the ground?", "Under"),
    ("Color of a strawberry?", "Red"),
    ("Direction of the wind?", "Varies"),
    ("Color of the night sky?", "Black"),
    ("Shape of a heart?", "Heart"),
    ("Color of a sunflower?", "Yellow"),
    ("Taste of peanut butter?", "Nutty"),
    ("Sound of a cat?", "Meow"),
    ("Touch of wool?", "Warm"),
    ("State of mercury at room temperature?", "Liquid"),
    ("Position of a tree?", "Ground"),
    ("Color of a blueberry?", "Blue"),
    ("Direction of lightning?", "Down"),
    ("Color of a mouse?", "Gray"),
    ("Shape of a star?", "Star"),
    ("Color of chocolate?", "Brown"),
    ("Taste of coffee?", "Bitter"),
    ("Sound of a train?", "Choo-choo"),
    ("Touch of glass?", "Smooth"),
    ("State of a computer chip?", "Solid"),
    ("Position of an airplane?", "Sky"),
    ("Color of a cherry?", "Red"),
    ("Direction of a car's movement?", "Forward"),
    ("Color of the ocean at night?", "Dark"),
    ("Shape of a hexagon?", "Hexagonal"),
    ("Color of a pumpkin?", "Orange"),
    ("Taste of grapefruit?", "Bitter"),
    ("Sound of a bird?", "Chirp"),
    ("Touch of leather?", "Smooth"),
    ("State of water vapor?", "Gas"),
    ("Position of a ship?", "Water"),
    ("Color of a plum?", "Purple"),
    ("Direction of a plane's ascent?", "Up"),
    ("Color of sand?", "Beige"),
    ("Shape of a pentagon?", "Pentagonal"),
    ("Color of a rose at night?", "Dark"),
    ("Taste of mint?", "Minty"),
    ("Sound of a bee?", "Buzz"),
    ("Touch of marble?", "Cold"),
    ("State of carbon dioxide at room temperature?", "Gas"),
    ("Position of a kangaroo?", "Ground"),
    ("Color of a grape?", "Purple"),
    ("Direction of a river?", "Flow"),
    ("Color of a turtle?", "Green"),
    ("Shape of an oval?", "Oval"),
    ("Color of a kiwi?", "Brown"),
    ("Taste of tea?", "Bitter"),
    ("Sound of a frog?", "Croak"),
    ("Touch of clay?", "Smooth"),
    ("State of a diamond?", "Solid"),
    ("Position of a kite?", "Sky"),
    ("Color of a peacock?", "Blue"),
    ("Direction of a fish's swim?", "Forward")
]

#========================================Display part===========================================================
general_questions_with_options = [
    ("Color of the sky?", ["Red", "Green", "Blue"]),
    ("Shape of the Earth?", ["Round", "Square", "Flat"]),
    ("Color of grass?", ["Yellow", "Blue", "Green"]),
    ("Taste of salt?", ["Bitter", "Salty", "Sweet"]),
    ("Sound of thunder?", ["Whisper", "Silent", "Loud"]),
    ("Touch of fire?", ["Smooth", "Cold", "Hot"]),
    ("State of water at 0°C?", ["Liquid", "Ice", "Gas"]),
    ("Position of the sun at noon?", ["Top", "Bottom", "Side"]),
    ("Color of a banana?", ["Red", "Yellow", "Blue"]),
    ("Direction of sunrise?", ["East", "West", "North"]),
    ("Color of the ocean?", ["Blue", "Red", "Black"]),
    ("Shape of a wheel?", ["Round", "Triangle", "Square"]),
    ("Color of an apple?", ["Green", "Red", "Blue"]),
    ("Taste of sugar?", ["Salty", "Sweet", "Bitter"]),
    ("Sound of rain?", ["Pitter-patter", "Silent", "Roar"]),
    ("Touch of ice?", ["Cold", "Hot", "Rough"]),
    ("State of water at 100°C?", ["Ice", "Liquid", "Steam"]),
    ("Position of the moon at night?", ["Ground", "Sea", "Sky"]),
    ("Color of an orange?", ["Orange", "Blue", "Green"]),
    ("Direction of sunset?", ["East", "West", "North"]),
    ("Color of a leaf?", ["Blue", "Red", "Green"]),
    ("Shape of a square?", ["Round", "Triangle", "Square"]),
    ("Color of snow?", ["Black", "White", "Yellow"]),
    ("Taste of lemon?", ["Sweet", "Sour", "Salty"]),
    ("Sound of a bell?", ["Whisper", "Roar", "Ring"]),
    ("Touch of sandpaper?", ["Smooth", "Rough", "Soft"]),
    ("State of water at room temperature?", ["Steam", "Ice", "Liquid"]),
    ("Position of stars?", ["Ground", "Sky", "Sea"]),
    ("Color of coal?", ["Red", "Black", "White"]),
    ("Direction of a compass needle?", ["North", "West", "East"]),
    ("Color of a rose?", ["Red", "Yellow", "Blue"]),
    ("Shape of a triangle?", ["Round", "Square", "Triangular"]),
    ("Color of honey?", ["Gold", "Blue", "Green"]),
    ("Taste of chocolate?", ["Salty", "Sweet", "Bitter"]),
    ("Sound of a car horn?", ["Silent", "Honk", "Whisper"]),
    ("Touch of a feather?", ["Rough", "Soft", "Hot"]),
    ("State of butter in the fridge?", ["Solid", "Gas", "Liquid"]),
    ("Position of clouds?", ["Sea", "Ground", "Sky"]),
    ("Color of a flamingo?", ["Pink", "Green", "Blue"]),
    ("Direction of river flow?", ["Upstream", "Downstream", "Sideways"]),
    ("Color of a frog?", ["Blue", "Red", "Green"]),
    ("Shape of a rectangle?", ["Square", "Round", "Rectangular"]),
    ("Color of the moon?", ["White", "Black", "Red"]),
    ("Taste of vinegar?", ["Sour", "Salty", "Sweet"]),
    ("Sound of a clock?", ["Roar", "Tick", "Whisper"]),
    ("Touch of velvet?", ["Hot", "Soft", "Rough"]),
    ("State of iron at room temperature?", ["Liquid", "Solid", "Gas"]),
    ("Position of the sun at sunset?", ["Top", "Side", "Horizon"]),
    ("Color of an egg yolk?", ["Green", "Yellow", "Blue"]),
    ("Direction of a bird's flight?", ["Up", "Down", "Side"]),
    ("Color of a carrot?", ["Red", "Orange", "Blue"]),
    ("Shape of a diamond?", ["Round", "Square", "Diamond"])
]



#========================================Main Code===========================================================

import random as rd
import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="🎉 Quiz Game", page_icon="🧠", layout="centered")

st.title("🎮 **Quiz Game** 🧠")
st.write("Welcome to the **Quiz Game**! 🌟 Test your knowledge and see how many questions you can get right. 💪")

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_active" not in st.session_state:
    st.session_state.game_active = True
if "correct_answered" not in st.session_state:
    st.session_state.correct_answered = False


answers = dict(data)

# Function to pick a new question
def pick_new_question():
    st.session_state.current_question = rd.choice(general_questions_with_options)
    st.session_state.correct_answered = False

# Start or continue the game
if st.session_state.game_active:
    # Pick a new question if none exists
    if not st.session_state.current_question:
        pick_new_question()

    # Display the current question
    question, options = st.session_state.current_question
    st.subheader(f"🧐 **Question:** {question}")
    selected_option = st.radio("🔍 Choose your answer:", options)

    # Submit button with interaction
    if st.button("✅ Submit") and not st.session_state.correct_answered:
        # Check the answer
        correct_answer = answers.get(question)
        if selected_option == correct_answer:
            st.session_state.score += 1
            st.session_state.correct_answered = True
            st.success(f"🎉 Correct! Your score: **{st.session_state.score}** 💯")
        else:
            st.error(f"❌ Incorrect! The correct answer was: **{correct_answer}**.")
            st.session_state.game_active = False

    # Show "Next" button if the answer is correct
    if st.session_state.correct_answered:
        if st.button("➡️ Next Question"):
            pick_new_question()
            st.rerun()

# Display "Play Again" option if the game is over
if not st.session_state.game_active:
    st.write("😢 **Game Over!** Want to try again?")
    if st.button("🔄 Play Again"):
        st.session_state.score = 0
        st.session_state.game_active = True
        st.session_state.current_question = None
        st.session_state.correct_answered = False
        st.rerun()


