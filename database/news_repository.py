from database.db import get_connection
def insert_dataframe(df):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO news_articles
    (
        title,
        description,
        source,
        published_at
    )
    VALUES (%s,%s,%s,%s)
    ON CONFLICT (title) DO NOTHING;
    """

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                row["title"],
                row["description"],
                row["source"],
                row["publishedAt"]
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

def get_articles_for_analysis():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

    id,

    title,

    description

    FROM news_articles

    WHERE category IS NULL

    """)

    rows = cursor.fetchall()

    cursor.close()

    conn.close()

    return rows

def update_analysis(
        article_id,
        category,
        sentiment,
        summary
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE news_articles

        SET

        category=%s,

        sentiment=%s,

        summary=%s

        WHERE id=%s
        """,

        (
            category,
            sentiment,
            summary,
            article_id
        )
    )

    conn.commit()

    cursor.close()

    conn.close()


import pandas as pd

def get_all_news():

    conn = get_connection()

    query = """
    SELECT
    title,
    description,
    source,
    category,
    sentiment,
    summary
    FROM news_articles
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df