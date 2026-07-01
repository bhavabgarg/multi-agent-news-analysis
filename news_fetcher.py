import requests
import os
from dotenv import load_dotenv
load_dotenv()
# limit for news 
def fetch_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = (
    f"https://newsapi.org/v2/everything"
    f"?q=technology OR business OR sports"
    f"&language=en"
    f"&sortBy=publishedAt"
    f"&pageSize=50"
    f"&apiKey={api_key}"
)
    
    response = requests.get(url)
    
    data = response.json()
    return data['articles']