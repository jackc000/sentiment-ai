from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    polarity, subjectivity = analyze_sentiment(sentence)
    print(f"Sentiment polarity: {polarity}")
    print(f"Sentiment subjectivity: {subjectivity}")
