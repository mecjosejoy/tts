import os
from pydub import AudioSegment


def merge_audios(input_folder, output_file):
    # Initialize an empty AudioSegment
    combined = AudioSegment.empty()

    # List all files in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".wav"):
            file_path = os.path.join(input_folder, filename)
            audio = AudioSegment.from_wav(file_path)
            combined += audio
            print(f"Added {filename} to the combined audio.")

    # Export the combined audio
    combined.export(output_file, format="wav")


input_folder = "output"  # Replace with your folder path
output_file = os.path.join(input_folder, "0.wav")

merge_audios(input_folder, output_file)
