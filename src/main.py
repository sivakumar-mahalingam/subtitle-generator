import subprocess
import os
import whisper
import srt
import torch
from datetime import timedelta

# Define the paths to the video file, subtitle file, and audio file
home_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
video_file = home_folder + '/data/GET_UP_AND_GET_IT_DONE.mp4'
srt_file = home_folder + '/data/GET_UP_AND_GET_IT_DONE.srt'
audio_file = home_folder + '/data/GET_UP_AND_GET_IT_DONE.wav'


def extract_audio():
    """
    Extracts audio from the video file and saves it as a .wav file using ffmpeg.

    Args:
        None

    Returns:
        None
    """
    # Define the ffmpeg command to extract the audio
    command = ['ffmpeg', '-y', '-i', video_file, '-q:a', '0', '-map', 'a', audio_file, '-loglevel', 'quiet']
    # Run the ffmpeg command
    subprocess.run(command)


def transcribe_audio_with_timestamp():
    """
    Transcribes the audio file and returns the transcription segments with timestamps.

    Args:
        None

    Returns:
        segments (list): A list of segments, each of which contains the start time, end time, and text of a segment of the audio.
    """
    # Load the whisper model
    model = whisper.load_model("base")
    # Check if CUDA is available and set the fp16 flag accordingly
    is_fp16 = True if torch.cuda.is_available() else False
    # Transcribe the audio file
    result = model.transcribe(audio_file, verbose=True, fp16=is_fp16)

    # Return the list of segments
    return result["segments"]


def create_srt_with_timestamp(segments):
    """
    Create an SRT file with the transcriptions and timestamps.

    Args:
        segments (list): A list of segments, each of which contains the start time, end time, and text of a segment of the audio.

    Returns:
        None
    """
    # Create an empty list to store the subtitles
    subtitles = []

    # Loop through the segments and create a subtitle for each one
    for segment in segments:
        start_time = timedelta(seconds=segment["start"])
        end_time = timedelta(seconds=segment["end"])
        text = segment["text"].strip()
        subtitle = srt.Subtitle(index=len(subtitles) + 1, start=start_time, end=end_time, content=text)
        subtitles.append(subtitle)

    # Compose the subtitles into a subtitle file
    srt_content = srt.compose(subtitles)
    # Write the subtitle file to disk
    with open(srt_file, 'w', encoding='UTF-8') as f:
        f.write(srt_content)


def generate_subtitles():
    """
    Generate the subtitles by calling the other functions in the correct order.

    Args:
        None

    Returns:
        None
    """
    # Extract the audio from the video file
    extract_audio()
    # Transcribe the audio file into text with timestamps
    segments = transcribe_audio_with_timestamp()
    # Create an SRT file with the transcriptions and timestamps
    create_srt_with_timestamp(segments)


# Call the generate_subtitles function if the script is run directly
if __name__ == "__main__":
    generate_subtitles()