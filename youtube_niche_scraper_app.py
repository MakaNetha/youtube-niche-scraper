import streamlit as st
import pandas as pd
import random
import datetime

# ---------- Simulated Trending Niches ----------
SIMULATED_NICHES = [
    {
        "niche": "AI Productivity Tools",
        "rpm": "$15.40",
        "example_channels": ["Ali Abdaal", "Thomas Frank Explains"],
        "thumbnail_idea": "Split screen showing old method vs. AI tool",
        "title_idea": "I Let AI Organize My Life for 30 Days… Here’s What Happened",
        "retention_strategy": "Start with a bold claim, break video into mini-chapters, cliffhangers before transitions."
    },
    {
        "niche": "Minimalist Lifestyle",
        "rpm": "$8.75",
        "example_channels": ["Matt D'Avella", "Pick Up Limes"],
        "thumbnail_idea": "Clean white background with bold black text overlay",
        "title_idea": "I Got Rid of 90% of My Stuff",
        "retention_strategy": "Use storytelling + before/after shots, show progressive results to keep viewer watching."
    },
    {
        "niche": "Faceless Luxury Relaxation Videos",
        "rpm": "$6.90",
        "example_channels": ["Scenic Relaxation", "Nomadic Ambience"],
        "thumbnail_idea": "Ocean waves with gold text overlay",
        "title_idea": "Luxury Coastal Walk – Relaxing Ambience 4K",
        "retention_strategy": "Looped, calming visuals and music, no jarring transitions. Create playlists to increase session time."
    }
]

# ---------- Prompt Generator ----------
def generate_video_prompt(niche):
    templates = [
        f"What are 5 things people don't know about {niche}?",
        f"A day in the life of someone obsessed with {niche}.",
        f"What if {niche} disappeared tomorrow?",
        f"Exposing the truth behind {niche}.",
        f"Top 3 ways to make money with {niche}."
    ]
    return random.choice(templates)

# ---------- Streamlit UI ----------
st.set_page_config(page_title="YouTube Niche Scraper App", layout="wide")
st.title("📈 YouTube Niche Scraper & Analyzer")

st.markdown("""
Welcome, Naeem! This tool simulates trending YouTube niches and helps you:
- 🧠 Discover ideas
- 🎯 Create title/thumbnail hooks
- 🔁 Improve retention
- 💰 Understand potential RPM
- 📤 Export everything as CSV
""")

if st.button("🔍 Show Trending Niches"):
    st.subheader("🔥 Trending Niches & Insights")
    df = pd.DataFrame(SIMULATED_NICHES)
    st.dataframe(df)

    if st.button("📤 Export as CSV"):
        df.to_csv("niche_report.csv", index=False)
        with open("niche_report.csv", "rb") as f:
            st.download_button(label="Download Niche Report", data=f, file_name="niche_report.csv", mime="text/csv")

st.markdown("---")
st.subheader("💡 Generate a Faceless Video Prompt")

selected_niche = st.selectbox("Choose a niche", [n["niche"] for n in SIMULATED_NICHES])
if st.button("🎬 Generate Prompt"):
    prompt = generate_video_prompt(selected_niche)
    st.success(prompt)

st.markdown("---")
st.caption(f"Built with 💻 by Naeem • {datetime.datetime.now().year}")
