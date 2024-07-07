# Subtitle Generator

This repository provides a Python script to generate subtitle files (`.srt`) for a given video file. The script extracts audio from the video, transcribes the audio using OpenAI's Whisper model, and generates an `.srt` file with the transcription and timestamps.

## SRT Files

SRT (.srt) files are the most common type of closed caption file format. SRT stands for “SubRip Subtitle” file.

An SRT file includes:

- The number of the closed caption frame in sequence
- Beginning and end timecodes for when the closed caption frame should appear
- The closed caption itself
- A blank link to indicate the start of a new closed caption sequence

![img.png](docs%2Fimg.png)

## Features

- Extracts audio from video files using `ffmpeg`.
- Transcribes audio to text with timestamps using OpenAI's Whisper model.
- Generates `.srt` subtitle files.

## Requirements

- `Python 3.7+`
- `ffmpeg`
- `torch`
- `openai-whisper`

## Installation

1. **Install `ffmpeg`**: 

   Make sure `ffmpeg` is installed on your system. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

2. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/subtitle-generator.git
   cd subtitle-generator
   ```

3. **Create a virtual environment and activate it**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Provide the path to the video file**:

   Ensure you have the video file path ready. The script will process this file to generate subtitles.

2. **Run the script**:
   
   Update all file paths (.srt, .wav, .mp4) in the script
   ```bash
   python generate_subtitles.py
   ```

3. **Output**:

   The script will create a `.srt` file with the same name as the video file in the same directory.

## Script Overview

### `generate_subtitles.py`

This is the main script that performs the following steps:

1. **Extract audio from the video file**:
   
   Uses `ffmpeg` to extract audio from the provided video file and save it as a `.wav` file.

2. **Transcribe the audio file**:
   
   Utilizes OpenAI's Whisper model to transcribe the audio into text with timestamps.

3. **Create the `.srt` file**:
   
   Generates an `.srt` file with the transcribed text and timestamps.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model.
- [ffmpeg](https://ffmpeg.org/) for audio extraction.


