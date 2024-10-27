import yt_dlp

def download_video(url, output_path='.'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,  
        'progress_hooks': [hook]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def hook(d):
    if d['status'] == 'finished':
        print(f"\nDone downloading video: {d['filename']}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
