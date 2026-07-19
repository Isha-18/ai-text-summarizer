import streamlit as st
from ai_client import summarize_article

st.title("📝 AI Text Summarizer")

user_input = st.text_area(
    "Paste your article",
    height=300,
    placeholder="Paste any article here..."
)

if st.button("Summarize"):

    if not user_input.strip():
        st.warning("Please enter an article.")
        st.stop()

    with st.spinner("Summarizing..."):

        try:

            result = summarize_article(user_input)

            st.subheader("📝 Summary")
            st.write(result["summary"])

            st.subheader("📌 Bullet Points")

            for point in result["bullet_points"]:
                st.write(f"• {point}")

            st.subheader("🏷 Keywords")
            st.write(", ".join(result["keywords"]))

        except Exception as e:

            st.error(str(e))

with st.sidebar:

    st.header("Settings")

    summary_length = st.selectbox(
        "Summary Length",
        ["Short", "Medium", "Detailed"]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.2
    )

    max_words = st.slider(
        "Maximum Words",
        50,
        500,
        150
    )