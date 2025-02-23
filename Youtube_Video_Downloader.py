import yt_dlp

def download_video():
    try:
        # Get YouTube URL from user input
        url = input("Enter the YouTube video URL: ")

        # Define options for yt-dlp to download both video and audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download best video and best audio
            'outtmpl': 'video_with_audio.mp4',     # Output filename
            'noplaylist': True,                    # Ensure we're downloading only one video
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video and audio
            ydl.download([url])
            print("\nDownload complete!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the download function
download_video()
