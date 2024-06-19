import pandas as pd
from gtts import gTTS
from pydub import AudioSegment
import os

proxy = "http://tmglotxc-rotate:stlrhx17nhqj@p.webshare.io:80/"

os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# Function to read the CSV file and convert each row to speech
def csv_to_speech(csv_file, language="ta", output_dir="output"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the CSV file
    df = pd.read_csv(csv_file, header=None)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        text = str(row[0])
        if len(text) == 0:
            continue
        
        if os.path.exists(os.path.join(output_dir, f"{index + 1}.wav")):
            print(f"Skipping {index + 1}.wav as it already exists")
            continue

        # Convert text to speech and save as MP3
        tts = gTTS(text=text, lang=language)
        mp3_file = os.path.join(output_dir, f"{index + 1}.mp3")
        tts.save(mp3_file)

        # Convert MP3 to WAV
        wav_file = os.path.join(output_dir, f"{index + 1}.wav")
        AudioSegment.from_mp3(mp3_file).export(wav_file, format="wav")

        # Optionally, remove the MP3 file
        os.remove(mp3_file)

        print(f"Saved {wav_file}")
        #eturn wav_file


# Example usage
csv_file_path = "Speech - Sheet1.csv"  # Replace with your actual CSV file path
csv_to_speech(csv_file_path)
