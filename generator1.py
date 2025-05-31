# generator.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_youtube_content(topic, audience, tone, language):
    prompt = f"""
    Create a YouTube video:
    - Topic: {topic}
    - Audience: {audience}
    - Tone: {tone}
    - Language: {language}
    
    Return the following:
    TITLE:
    DESCRIPTION:
    SCRIPT:
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative YouTube content writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        content = response.choices[0].message.content
        parts = content.split("SCRIPT:")
        desc_title = parts[0].split("DESCRIPTION:")
        title = desc_title[0].replace("TITLE:", "").strip()
        description = desc_title[1].strip()
        script = parts[1].strip()

        return title, description, script

    except Exception as e:
        raise Exception("Failed to generate content: " + str(e))
