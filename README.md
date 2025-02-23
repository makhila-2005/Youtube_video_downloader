# Youtube_video_downloader

# YouTube Video Downloader 📩

This is a simple **Streamlit** web application that allows users to download YouTube videos with both video and audio using **yt-dlp** and **ffmpeg**. The app allows users to enter a YouTube URL and download the video in the best available quality.

## Features:
- **Download YouTube videos**: Get both video and audio from YouTube in the highest available quality.
- **User-friendly interface**: Built using Streamlit for a smooth and simple experience.
- **Instant download**: Just input a valid YouTube URL and start the download process with a button click.

## Requirements:
You’ll need Python installed on your computer, along with the following dependencies:
- **yt-dlp**: For downloading YouTube videos and audio.
- **Streamlit**: For creating the web application interface.
- **ffmpeg**: For merging audio and video.

To install the dependencies, run this command in your terminal or command prompt:

```bash
pip install yt-dlp streamlit
```

## How to Run the App:
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project folder.
3. Install the required dependencies:
   ```bash
   pip install yt-dlp streamlit
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run Youtube_Video_Downloader.py
   ```

5. The app will open in your default web browser. If it doesn’t open automatically, you can visit `http://localhost:8501`.

## How to Use the App:
1. Enter the YouTube video URL/ YouTube playlist URL in the provided input field.
2. Click the **Download Video** button.
3. The app will start downloading the video along with its audio. Once complete, you’ll see a confirmation message.

## Example:
- **URL**: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- **Result**: Download complete! 🎊.

## Troubleshooting:
- Make sure you have a stable internet connection.
- Ensure the YouTube URL is valid and accessible.
- If you encounter any issues with the download, check the terminal for detailed error messages.



---
