def generate_content(topic, audience, tone, language):
    title = f"Interesting Insights on {topic}"
    description = (
        f"This video explores the topic of {topic} aimed at {audience}. "
        f"The content is delivered in a {tone.lower()} tone and presented in {language}."
    )
    script = (
        f"Hello everyone! Welcome to our channel.\n\n"
        f"Today, we're diving into the fascinating topic of {topic}. "
        f"This discussion is tailored especially for {audience}, and you'll find the tone to be {tone.lower()} throughout.\n\n"
        f"Let's start by understanding the basics of {topic}.\n\n"
        f"[Explain key points about {topic} here...]\n\n"
        f"To sum up, {topic} is an exciting subject that offers a lot of value to {audience}.\n\n"
        f"Thank you for watching! Don't forget to like, share, and subscribe for more insightful videos."
        f"If you're following along, let us know in the comments below — what part of {topic} surprised you the most?\n\n"
        f"Thanks a ton for watching. Don’t forget to **like, share**, and **subscribe** for more insightful content.\n"
    )
    return title, description, script




