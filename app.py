import os
import streamlit as st
from datetime import datetime
import openai

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Social Media Agent", layout="centered")

st.title("Social Media Agent — Caption, Hashtags & Content Plan Generator")
st.markdown("Generate captions, hashtags, and weekly content plans using OpenAI.")

# Sidebar Settings
st.sidebar.header("Settings")
platform = st.sidebar.selectbox("Platform", ["Instagram", "Twitter/X", "LinkedIn", "Facebook", "TikTok", "YouTube"], index=0)
num_posts = st.sidebar.slider("Posts per week", 1, 14, 5)
tone = st.sidebar.selectbox("Tone", ["Casual", "Professional", "Inspiring", "Funny", "Informative"], index=0)

# Main Input
st.header("Generate Captions & Hashtags")
topic = st.text_area("Enter Post Topic", height=120)

if st.button("Generate Output"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            prompt = f"Write 5 captions, 15 hashtags, and 5 CTAs for this topic: {topic}. Platform: {platform}. Tone: {tone}. Return in JSON with keys: captions, hashtags, ctas."

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response['choices'][0]['message']['content']
            st.code(output)

# Weekly Plan
st.header("Weekly Content Plan")
plan_topic = st.text_input("Weekly Theme (example: Travel Week, Fitness Tips)")

if st.button("Generate Weekly Plan"):
    if not plan_topic.strip():
        st.warning("Enter a weekly theme.")
    else:
        prompt2 = f"Create a {num_posts}-post content plan for {platform} on theme: {plan_topic}. Include title, caption, post type, 5 hashtags, and CTA."

        resp2 = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt2}]
        )

        st.code(resp2['choices'][0]['message']['content'])
