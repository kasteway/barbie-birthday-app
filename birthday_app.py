#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
import streamlit as st

# Add custom CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://i.pinimg.com/originals/dc/6c/97/dc6c97c818f08995cb8e55d4d7b75f7f.jpg'); /* Barbie-themed background */
        background-size: cover;
        color: #ff69b4; /* Barbie pink text */
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Fun font */
    }
    .stButton>button {
        background-color: #ff69b4; /* Barbie pink button */
        color: white;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #ff69b4;
        margin-bottom: 20px;
        text-shadow: 2px 2px #ffffff;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #ff69b4;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title with fun styling
st.markdown('<h1 class="title">🎀 Special GIRLS Birthday Countdown 🎂</h1>', unsafe_allow_html=True)

# Barbie GIF or image
st.image(
    "https://media0.giphy.com/media/l0IybQ6l8nfKjxQv6/200.webp?cid=bb5a1c3avrdvnx41ptseeuo74954ue36c1rdeqr7d5qvryqt&ep=v1_gifs_trending&rid=200.webp&ct=g/giphy.gif",  # New Barbie GIF
    width=350,
)
st.markdown('<h1 class="title">🎀 Let\'s count down to your birthday! 💖 🎂</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="title">🎀 Made with ❤️ for special BABIES! 🎂</h1>', unsafe_allow_html=True)

# Input for name
name = st.text_input("What's your name?", placeholder="Enter your name 💕")

# Input for next birthday
birthday = st.date_input("Pick your next birthday 📅", value=date.today())

# "Done" button to confirm date
if st.button("Done"):
    if name:
        # Calculate days left
        today = date.today()
        days_left = (birthday - today).days

        # Display countdown message with title styling
        if days_left < 0:
            st.markdown('<h1 class="title">🎀 Hi {name}, your birthday has already passed this year! 💕 🎂</h1>'.format(name=name), unsafe_allow_html=True)
        elif days_left == 0:
            st.markdown('<h1 class="title">🎀 Happy Birthday, {name}! 🎉🎂✨ 🎂</h1>'.format(name=name), unsafe_allow_html=True)
        else:
            st.markdown('<h1 class="title">🎀 Hi {name}, there are **{days_left} days** left until your birthday! 🎈💐 🎂</h1>'.format(name=name, days_left=days_left), unsafe_allow_html=True)
    else:
        st.write("Please enter your name to continue! 🌟")

# "Celebrate Anyway!" button
if st.button("🎉 Celebrate it\'s my bday!"):
    st.markdown('<h1 class="title">🎀 It\'s always a good time to celebrate ME because I AM NOT DEAD yet! 💖✨ 🎂</h1>', unsafe_allow_html=True)
    st.image(
        "https://media4.giphy.com/media/CDNfxKfNlrPFj2J9US/200w.webp?cid=bb5a1c3avrdvnx41ptseeuo74954ue36c1rdeqr7d5qvryqt&ep=v1_gifs_trending&rid=200w.webp&ct=g/giphy.gif",  # New Barbie GIF
        caption="Woohoo! Let’s Celebrate 🎈🎉",
        use_container_width=True,
    )
    st.balloons()
    st.snow()

# Always available "Celebrate Anytime!" button
if st.button("🎉 Celebrate Anytime!"):
    st.markdown('<h1 class="title">🎀 It\'s always a good time to celebrate ME because I AM NOT DEAD yet! 🎂</h1>', unsafe_allow_html=True)
    st.image(
        "https://media4.giphy.com/media/CDNfxKfNlrPFj2J9US/200w.webp?cid=bb5a1c3avrdvnx41ptseeuo74954ue36c1rdeqr7d5qvryqt&ep=v1_gifs_trending&rid=200w.webp&ct=g/giphy.gif",  # New Barbie GIF
        caption="Celebrate for Fun! 🎈💃",
        use_container_width=True,
    )
    st.balloons()
    st.snow()

# Footer
st.markdown('<h1 class="title">🎀 Made with ❤️ for special BABIES! 🎂</h1>', unsafe_allow_html=True)

