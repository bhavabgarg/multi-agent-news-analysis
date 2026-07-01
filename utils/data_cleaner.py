import pandas as pd


def clean_news_data(articles):

    df = pd.DataFrame(articles)

    print("Original Records:", len(df))

    # Select required columns
    df = df[
        [
            "title",
            "description",
            "publishedAt",
            "source"
        ]
    ]

    # Extract source name
    df["source"] = df["source"].apply(
        lambda x: x["name"] if x else "Unknown"
    )

    # Remove rows with no title
    df = df.dropna(subset=["title"])

    # Fill missing description
    df["description"] = df[
        "description"
    ].fillna("No Description Available")

    # Remove duplicates
    df = df.drop_duplicates(
        subset=["title"]
    )

    # Remove extra spaces
    df["title"] = df["title"].str.strip()

    df["description"] = (
        df["description"].str.strip()
    )

    print("Cleaned Records:", len(df))

    return df

def save_clean_data(df):

    df.to_csv(
        "data/clean_news.csv",
        index=False
    )

    print("CSV Saved")