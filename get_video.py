import os
from pytube import YouTube

def download_youtube_video(url, output_path='videos'):
    """
    Download a video from YouTube to the specified output path.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
    if stream:
        print(f"Downloading: {yt.title}")
        stream.download(output_path=output_path)
        print(f"Downloaded to {output_path}")
    else:
        print("No suitable stream found.")

if __name__ == "__main__":
    # Example usage: replace with your desired YouTube video URL
    video_url = input("Enter YouTube video URL: ")
    download_youtube_video(video_url) 