

import yt_dlp
import streamlit as st
import os

def download_video(url):
    try:
        # Define options for yt-dlp to download both video and audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download best video and best audio
            
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video and audio
            ydl.download([url])
        return "Download complete! 🎊"
    except Exception as e:
        return f"Error occurred: {e}"

# Streamlit UI
st.title("YouTube Video Downloader📩")
st.write("Enter a YouTube URL to download the video with audio.")

# Input field for the YouTube URL
url = st.text_input("Enter the YouTube video URL:")

# Button to start the download process
if st.button('Download Video'):
    if url:
        st.write("Downloading, please wait...")
        result_message = download_video(url)
        st.success(result_message)
    else:
        st.warning("Please enter a valid YouTube URL.")
