from news_fetcher import fetch_news
from utils.data_cleaner import clean_news_data
from database.news_repository import insert_dataframe

from main_analysis import run_analysis


def run_pipeline():

    print("STEP 1: Fetch News")

    articles = fetch_news()

    print("STEP 2: Clean Data")

    df = clean_news_data(articles)

    print("STEP 3: Insert")

    insert_dataframe(df)

    print("STEP 4: AI Analysis")

    run_analysis()

    print("Pipeline Finished")