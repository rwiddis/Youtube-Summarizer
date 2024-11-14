```markdown
# YouTube Video Summarizer

A Python script that automatically generates detailed summaries of YouTube videos using their transcripts and GPT-4-mini.

## Features

- Extracts video transcripts from any YouTube video URL using [`get_video_transcript`](summarize.py)
- Supports both youtube.com and youtu.be URL formats via [`get_video_id`](summarize.py)
- Generates comprehensive summaries using OpenAI's GPT-4-mini model through [`generate_summary`](summarize.py)
- Handles errors gracefully with informative messages

## Prerequisites

- Python 3.x
- OpenAI API key
- Required packages: `youtube-transcript-api`, `openai`

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd youtube-summarizer
```

2. Install required packages:
```sh
pip install youtube-transcript-api openai
```

3. Set up your OpenAI API key as an environment variable:
```sh
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Run the script:
```sh
python summarize.py
```

When prompted, enter a YouTube video URL. The script will:
1. Extract the video ID
2. Fetch the video transcript
3. Generate a detailed summary using GPT-4-mini
4. Display the summary in the console

## Code Structure

The main functionality is implemented in 

summarize.py

 with these key functions:
- `get_video_id`: Extracts video ID from YouTube URLs
- `get_video_transcript`: Retrieves video transcript using YouTube API
- `generate_summary`: Generates summary using OpenAI API
- `summarize_video`: Main function that coordinates the summarization process

## Error Handling

The script handles various errors including:
- Invalid YouTube URLs
- Unavailable transcripts
- API failures

## License

MIT License

## Note

Make sure you have a valid OpenAI API key and sufficient credits for API usage.
```