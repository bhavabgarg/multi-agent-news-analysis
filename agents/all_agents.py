import json

from groq_llm import llm
from langchain_core.messages import HumanMessage


def analyze_news(title, description):

    prompt = f"""
You are a News Analysis Assistant.

Analyze the following news article.

Return ONLY valid JSON.

{{
  "category": "Technology | Business | Sports | Politics | Entertainment | Health",
  "sentiment": "Positive | Negative | Neutral",
  "summary": "Maximum 25 words"
}}

Title:
{title}

Description:
{description}

Do not return markdown.
Do not use ```json.
Return JSON only.
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    text = response.content.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)