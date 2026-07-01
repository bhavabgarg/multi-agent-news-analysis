import streamlit as st
from pipeline.pipeline import run_pipeline

from database.news_repository import get_all_news
import plotly.express as px

st.set_page_config(
    page_title="News Analysis Dashboard",
    layout="wide"
)

st.title("📰 Multi-Agent News Analysis Dashboard")

if st.button("🔄 Refresh Latest News"):

    with st.spinner("Updating latest news..."):

        run_pipeline()

    st.success("Pipeline Completed Successfully")

    st.rerun()
    
df = get_all_news()



col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Articles",
    len(df)
)

col2.metric(
    "Categories",
    df["category"].nunique()
)

col3.metric(
    "Sources",
    df["source"].nunique()
)

category_count = (
    df["category"]
    .value_counts()
    .reset_index()
)

category_count.columns = [
    "Category",
    "Count"
]

fig = px.bar(
    category_count,
    x="Category",
    y="Count",
    title="News by Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

sentiment_count = (
    df["sentiment"]
    .value_counts()
    .reset_index()
)

sentiment_count.columns = [
    "Sentiment",
    "Count"
]

fig2 = px.pie(
    sentiment_count,
    names="Sentiment",
    values="Count",
    title="Sentiment Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


search = st.text_input(
    "Search News"
)

if search:

    filtered = df[
        df["title"]
        .str.contains(
            search,
            case=False
        )
    ]

else:

    filtered = df

category = st.selectbox(

    "Category",

    ["All"] +
    list(df["category"].unique())
)

if category != "All":

    filtered = filtered[
        filtered["category"] == category
    ]

sentiment = st.selectbox(

    "Sentiment",

    ["All"] +
    list(df["sentiment"].unique())
)

if sentiment != "All":

    filtered = filtered[
        filtered["sentiment"] == sentiment
    ]

st.dataframe(
    filtered[
        [
            "title",
            "category",
            "sentiment"
        ]
    ]
)

st.header("News Summary")

for _, row in filtered.iterrows():

    with st.expander(row["title"]):

        st.write("Category:", row["category"])

        st.write("Sentiment:", row["sentiment"])

        st.write(row["summary"])