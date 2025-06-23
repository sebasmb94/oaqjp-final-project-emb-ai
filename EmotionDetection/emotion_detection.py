import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 400:

        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    else:
        formatted_response = json.loads(response.text)

        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        maxEmotion = ''
        maxScore = 0

        for key in emotions:
            if emotions[key] > maxScore:
                maxEmotion = key
                maxScore = emotions[key]

        emotions["dominant_emotion"] = maxEmotion

        return emotions

