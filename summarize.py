import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
    return None

def get_video_transcript(video_id):
    """Get video transcript using YouTube API"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([t['text'] for t in transcript_list])
        return transcript
    except Exception as e:
        print(f"Error getting transcript: {str(e)}")
        return None

def generate_summary(transcript):
    """Generate summary using OpenAI API"""
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    try:

        response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts.The summary does not need to be short, detail is encouraged to help users fully understand the video without watching it all. Elaborate on topics or acronyms that are not common knowledge where applicable. Include the tools used if applicable, preferred platforms or methods mentioned by the video."},
                {"role": "user", "content": f"Please provide a concise summary of the following transcript:\n{transcript}"}
                ],
                temperature=0.3,
                max_tokens=1000
            )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating summary: {str(e)}")
        return None

def summarize_video(url):
    """Main function to summarize YouTube video"""
    video_id = get_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"
    
    transcript = get_video_transcript(video_id)
    if not transcript:
        return "Could not retrieve video transcript"
    
    summary = generate_summary(transcript)
    if not summary:
        return "Could not generate summary"
    
    return summary

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube video URL: ")
    summary = summarize_video(video_url)
    print("\nSummary:")
    print(summary)