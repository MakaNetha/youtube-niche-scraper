# YouTube Niche Scraper + Analyzer

A Streamlit web app that:
- Scrapes trending YouTube videos
- Estimates RPM and potential earnings
- Suggests adjacent and evergreen content ideas
- Recommends retention strategies and hooks
- Downloads thumbnails
- Exports CSV reports

## 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run youtube_niche_scraper_app.py
```

## 🌐 Deploy to Streamlit Cloud
1. Add your API keys to Streamlit Secrets:
```
[general]
YOUTUBE_API_KEY = "your_youtube_api_key"
OPENAI_API_KEY = "your_openai_api_key"
```
2. Deploy directly from GitHub.
