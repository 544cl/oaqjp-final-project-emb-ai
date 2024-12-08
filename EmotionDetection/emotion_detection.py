import requests
import json
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ['anger','disgust','fear','joy','sadness']
def emotion_detector(text_to_analyse):
    if text_to_analyse is None or text_to_analyse == '':
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    response = requests.post(
        URL,
        headers=HEADERS,
        data = json.dumps({
            "raw_document": { "text": text_to_analyse }
        })
    )
    data = response.json()
    emotions = data['emotionPredictions'][0]['emotion']
    dominant_emotion = ''

    max_score = -1
    for em in EMOTIONS:
        if emotions[em] > max_score:
            dominant_emotion = em
            max_score = emotions[em]

    return {**emotions, 'dominant_emotion':dominant_emotion}


