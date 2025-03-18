from PIL import Image
import streamlit as st

# Page Config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# Title
st.title("🎉 Happy Birthday! 🎂")

# Load and display local image
image = Image.open("birthday_image.jpg")  # Make sure the name matches your file
image = image.resize((500, 500))  # Change width and height as needed

st.image(image, use_container_width=False) 
# Birthday Message
st.markdown(
    """
    <h2 style='text-align: center; color: #76d7c4;'>🎉 Happy Birthday! 🎂</h2>
    <p style='font-size:20px; text-align: center; color: #2E86C1;'>
        Wishing you a day filled with love, joy, and happiness! 🎈🎁❤️
    </p>
    """,
    unsafe_allow_html=True
)



# Footer Message
st.markdown(
    """
    <h2 style='text-align: center; color: #76d7c4;'>🎉 Turn 23 celebrates 💖
🎂</h2>
    <p style='font-size:25px; text-align: center; color: #2E86C1;'> 🎉 Happy 23rd Birthday! 🎂</p>

<p style='font-size:20px; text-align: center; color: #d35400;'> "May this special year bring you endless joy, exciting adventures, and countless achievements. At 23, you’re stepping into a phase of new opportunities, growth, and self-discovery. May every day be filled with love, laughter, and success. Keep shining, keep dreaming, and keep making beautiful memories!"</p>

<p style='font-size:20px; text-align: center; color: #1a5276'>✨ Wishing you happiness, good health, and all the success your heart desires! 💖

 🎈🎁❤️
    </p>
    """,
    unsafe_allow_html=True
)
