import json
import urllib.request
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('news-sentiment-history')

NEGATIVE_WORDS = ["war", "crisis", "crash", "attack", "death", "disaster", 
                  "threat", "conflict", "explosion", "killed", "chaos"]
POSITIVE_WORDS = ["peace", "growth", "recovery", "success", "victory", 
                  "breakthrough", "agreement", "hope", "progress", "wins"]

def analyze_sentiment(headlines):
    score = 0
    for headline in headlines:
        headline_lower = headline.lower()
        for word in NEGATIVE_WORDS:
            if word in headline_lower:
                score -= 1
        for word in POSITIVE_WORDS:
            if word in headline_lower:
                score += 1
    return score

def lambda_handler(event, context):
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=222e90ee9ae54c86ad03691c601cf68d"
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    
    headlines = [article['title'] for article in data['articles'][:10]]
    score = analyze_sentiment(headlines)
    
    if score >= 2:
        mood = "POSITIVE"
        color = "GREEN"
    elif score <= -2:
        mood = "NEGATIVE"
        color = "RED"
    else:
        mood = "NEUTRAL"
        color = "YELLOW"

    timestamp = datetime.now(timezone.utc).isoformat()
    
    table.put_item(Item={
        'timestamp': timestamp,
        'score': score,
        'mood': mood,
        'color': color,
        'headlines': headlines
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'timestamp': timestamp,
            'headlines': headlines,
            'score': score,
            'mood': mood,
            'color': color
        })
    }
