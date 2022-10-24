from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as vaderSentiment

def get_sentiment(text):
    analyzer = vaderSentiment()
    result = analyzer.polarity_scores(text)
    sentiment = None
    if result["compound"] >= 0.05:
        sentiment = "Positive"
    elif result["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return f"The sentiment of the text is: {sentiment}"
