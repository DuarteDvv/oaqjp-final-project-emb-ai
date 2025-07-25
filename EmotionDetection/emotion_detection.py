import requests
import json

def emotion_detector(text_to_analyse):
    
    # endpoint of ibm api
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # request metadata
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # input
    api_input = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }

    # request
    response = requests.post(url, json=api_input, headers=headers)

    if response.status_code == 400:

        return None
    
    # format to json
    formatted_response = json.loads(response.text)

    emotions_score = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions_score['anger']
    disgust_score = emotions_score['disgust']
    fear_score = emotions_score['fear']
    joy_score = emotions_score['joy']
    sadness_score = emotions_score['sadness']

    scores = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score
    }

    top_emotion = max(scores, key=scores.get)

    r =     {
        **scores,
        'dominant_emotion': top_emotion
    }

    return r