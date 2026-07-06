import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/raw_skills.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Fill missing values
df["Skills"] = df["Skills"].fillna("").astype(str)

# Create TF-IDF matrix
tfidf = TfidfVectorizer()
skill_matrix = tfidf.fit_transform(df["Skills"])

# Streamlit UI
st.title("🎯 AI Tech Stack Recommendation System")
st.write("Enter your technical skills and get the top 3 career recommendations using AI.")

skills = st.text_input("Enter your skills", placeholder="Example: Python, SQL, Machine Learning")

if st.button("Recommend"):

    if skills.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        user_text = skills.replace(",", " ")
        user_vector = tfidf.transform([user_text])

        similarity = cosine_similarity(user_vector, skill_matrix)
        df["Similarity"] = similarity.flatten()
        df["Match %"] = (df["Similarity"] * 100).round(2)

        result = df.sort_values(by="Similarity", ascending=False).head(3)

        st.success("Top 3 Career Recommendations")

        for index, row in result.iterrows():
            st.write(f"### {row['Job_Roles']}")
            st.write(f"✅ Match Percentage: {row['Match %']}%")
            st.write("---")
    user_text = skills.replace(",", " ")
    user_vector = tfidf.transform([user_text])

    similarity = cosine_similarity(user_vector, skill_matrix)
    df["Similarity"] = similarity.flatten()
    df["Match %"] = (df["Similarity"] * 100).round(2)

    result = df.sort_values(by="Similarity", ascending=False).head(3)

    st.subheader("Top 3 Career Recommendations")

    st.success("Top 3 Career Recommendations")

for index, row in result.iterrows():
    st.write(f"### {row['Job_Role']}")
    st.write(f"✅ Match Percentage: {row['Match %']}%")
    st.write("---")