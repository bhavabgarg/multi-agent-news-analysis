CREATE TABLE news_articles(
    id SERIAL PRIMARY KEY,

    title TEXT,

    description TEXT,

    source VARCHAR(100),

    published_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);