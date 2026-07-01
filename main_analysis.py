from agents.all_agents import analyze_news

from database.news_repository import (
    get_articles_for_analysis,
    update_analysis
)
from concurrent.futures import ThreadPoolExecutor

def process_article(article):

    article_id = article[0]

    title = article[1]

    description = article[2] or ""

    try:

        result = analyze_news(
            title,
            description
        )

        update_analysis(
            article_id,
            result["category"],
            result["sentiment"],
            result["summary"]
        )

        print(f"{article_id} Completed")

    except Exception as e:

        print(f"{article_id} Error: {e}")


def run_analysis():

    articles = get_articles_for_analysis()

    print(f"Articles Found: {len(articles)}")

    with ThreadPoolExecutor(max_workers=2) as executor:

        executor.map(process_article, articles)

    print("Analysis Completed")