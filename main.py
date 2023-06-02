import os
import subprocess

def convert_file(file_path):


  # Get the file extension.
  extension = os.path.splitext(file_path)[1]

  # Check if the file is an audio file.
  if extension in [".mp3", ".amr", ".m4a", ".mpa", ".aac",".ogg", ".3gpp"]:
    # Convert the file to WAV format.
    subprocess.call([
        "ffmpeg", "-i", file_path, "-c:a", "pcm_s16le", "-ar", "44100", "-ac", "2", "-b:a", "192k", os.path.join(os.path.dirname(file_path), os.path.basename(file_path) + ".wav")
    ])

def convert_folder(folder_path):


  # Get all files in the folder.
  files = os.listdir(folder_path)

  # Convert each file to WAV format.
  for file in files:
    convert_file(os.path.join(folder_path, file))

if __name__ == "__main__":
  # Get the folder path from the user.
  folder_path = "/content/drive/MyDrive/Bengali Accent Classification Dataset/regionData/Formal"

  # Convert all files in the folder to WAV format.
  convert_folder(folder_path)