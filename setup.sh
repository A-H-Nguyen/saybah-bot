#!/bin/bash

touch .env

# Create venv
python -m venv bot-env

# Create empty .env file -- need to manually put in bot token
touch .env

source activate

# Install requirements
pip install -r requirements.txt
pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz

# Check for ffmpeg install on system
if ! hash ffmpeg 2>/dev/null
then
    echo "No ffmpeg found in PATH"
else
    echo "ffmpeg found: "
    which ffmpeg
fi