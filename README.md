# CSV to Speech Conversion Script

This guide provides a full setup and usage guide for the CSV to Speech Conversion script. This script reads a CSV file, converts each row of text to speech using Google Text-to-Speech (gTTS), and saves the audio files in WAV format.

## Requirements

- Python 3.7 or later
- Required Python packages (specified in `requirements.txt`)

## Setup Guide

1. **Clone the Repository**

   If you haven't already, clone the repository to your local machine:

   ```bash
   git clone https://github.com/kevinnadar22/tts
   cd tts
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   It is recommended to create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Your CSV File**

   Ensure your CSV file is formatted correctly. Each row should contain the text you want to convert to speech. The script assumes there is no header row.

5. **Run the Script**

   Replace the `csv_file_path` variable in the script with the path to your CSV file. Then, run the script:

   ```bash
   python main.py
   ```

## Usage

The script will:

1. Read the CSV file specified by `csv_file_path`.
2. Convert each row of text to speech using the specified language (default is Tamil).
3. Save the audio files in the specified output directory (default is "output").

### Script Overview

```python
import pandas as pd
from gtts import gTTS
from pydub import AudioSegment
import os

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

# Example usage
csv_file_path = "Speech - Sheet1.csv"  # Replace with your actual CSV file path
csv_to_speech(csv_file_path)
```

## Customization

- **Change Language**: Modify the `language` parameter in the `csv_to_speech` function to change the language of the text-to-speech conversion. Refer to the gTTS documentation for supported languages.
- **Output Directory**: Change the `output_dir` parameter in the `csv_to_speech` function to specify a different output directory.

## Requirements.txt

The `requirements.txt` file should contain the following:

```
pandas
gTTS
pydub
```

Make sure you have `ffmpeg` installed as `pydub` relies on it for audio format conversion. You can install `ffmpeg` using:

- **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html).
- **macOS**: Install using Homebrew:

  ```bash
  brew install ffmpeg
  ```

- **Linux**: Install using your package manager, e.g., for Ubuntu:

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

## Troubleshooting

- **Permission Errors**: Ensure you have the necessary permissions to read the CSV file and write to the output directory.
- **Missing Dependencies**: Ensure all dependencies are installed correctly. Use `pip list` to check installed packages.
- **FFmpeg Issues**: Verify `ffmpeg` is installed and available in your system PATH.

