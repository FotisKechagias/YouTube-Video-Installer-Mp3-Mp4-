from pytubefix import YouTube
import os

def create_folders(base_path):
    """Ensures the download directories exist."""
    mp4_path = os.path.join(base_path, "Mp4")
    mp3_path = os.path.join(base_path, "Mp3")
    
    if not os.path.exists(mp4_path):
        os.makedirs(mp4_path)
    if not os.path.exists(mp3_path):
        os.makedirs(mp3_path)
        
    return mp4_path, mp3_path

def YtDownload():
    base_path = r"Your/path"
    mp4_dir, mp3_dir = create_folders(base_path)

    print("--- YouTube Downloader Started ---")
    print("Press Ctrl+C to exit anytime.\n")

    while True:
        try:
            url = ""
            while not url:
                url = input("Enter the URL: ").strip()
                if not url:
                    print("URL cannot be empty.")

            try:
                yt = YouTube(url)
                print(f"\nTitle: {yt.title}")

            except Exception as e:
                print(f"Error finding video: {e}")
                print("Please check the URL and try again.\n")
                continue

            choice = ""
            while choice not in ["mp4", "mp3"]:
                user_input = input("Download as mp4 or mp3?: ").strip().lower()
                if user_input in ["mp4", "mp3"]:
                    choice = user_input
                else:
                    print("Invalid choice. Please type 'mp4' or 'mp3'.")

            print("Downloading...")
            
            if choice == "mp4":
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=mp4_dir)
                print(f"Video saved to: {mp4_dir}")
                
            else:
                stream = yt.streams.get_audio_only()
                out_file = stream.download(output_path=mp3_dir)
                
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                
                if os.path.exists(new_file):
                    os.remove(new_file) 
                    
                os.rename(out_file, new_file)
                print(f"Audio saved to: {new_file}")

            print("\nDownload complete! Ready for next video.\n")

        except KeyboardInterrupt:
            print("\n\nExiting program. Goodbye!")
            break
        except Exception as e:
            print(f"\nA generic error occurred: {e}")
            print("Restarting loop...\n")

if __name__ == "__main__":
    YtDownload()