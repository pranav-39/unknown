import streamlit as st
import random
import requests

st.title("AI-Based Intoxication Detection Simulator")

image = st.file_uploader("Upload facial image (RGB/Thermal)", type=["jpg", "png"])
audio = st.file_uploader("Upload voice sample", type=["wav", "mp3"])

if st.button("Run Detection"):
    if image:
        prediction = random.choice(["Normal", "Alcohol-Intoxicated", "Drug-Intoxicated", "Mixed Intoxication"])
        confidence = round(random.uniform(80, 98), 2)

        st.success(f"Detected: {prediction} (Confidence: {confidence}%)")

        # Simulated IoT telemetry post (replace with your token)
        data = {
            "status": prediction,
            "confidence": confidence
        }

        try:
            requests.post("https://demo.thingsboard.io/api/v1/YOUR_TOKEN/telemetry", json=data)
            st.info("Data sent to ThingsBoard.")
        except:
            st.warning("Error sending to ThingsBoard.")
    else:
        st.error("Upload an image to simulate detection.")
