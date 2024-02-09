import streamlit as st
import json

# Read the JSON file containing the articles
with open('news_json.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Group the articles by cluster number
articles_by_cluster = {}
for article in articles:
    cluster = article['cluster']
    if cluster not in articles_by_cluster:
        articles_by_cluster[cluster] = []
    articles_by_cluster[cluster].append(article)

# Sort the cluster numbers
sorted_clusters = sorted(articles_by_cluster.keys())

# Create a Streamlit app
st.title('Articles by Cluster')

# Display articles by cluster
for cluster in sorted_clusters:
    cluster_articles = articles_by_cluster[cluster]
    st.header(f'Cluster {cluster}')
    for article in cluster_articles:
        st.subheader(f"[{article['title']}]({article['url']})")
        st.write(article['content'])
