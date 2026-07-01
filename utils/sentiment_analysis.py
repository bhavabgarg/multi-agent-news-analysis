import pandas as pd

from database.db import get_connection


def sentiment_summary():

    conn = get_connection()

    query = """
    SELECT sentiment
    FROM news_articles
    """

    df = pd.read_sql(query, conn)

    print("\nSentiment Distribution\n")

    print(df["sentiment"].value_counts())

    conn.close()