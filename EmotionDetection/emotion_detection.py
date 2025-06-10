import requests
import json

def emotion_detector( text_to_analyse ):
    """
    Function that analyzes the emotion of the given text

    Args:
        text_to_analyse (str) : The text to be analyzed

    return:
        text : Text returned by the API
    """
    # url of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #header required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #dict with the text to be evaluated
    myobj = json.dumps( { "raw_document": { "text": text_to_analyse } } )

    #POST request to the API
    response = requests.post( url, myobj, headers=header )

    #format the response
    formatted_response = json.loads( response.text )

    if response.status_code == 200:
        #extract scores from the response data
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        dominant_emotion = "anger"
        dominant_score = anger_score
        if dominant_score < disgust_score:
            dominant_score = disgust_score
            dominant_emotion = "disgust"
        if dominant_score < fear_score:
            dominant_score = fear_score
            dominant_emotion = "fear"
        if dominant_score < joy_score:
            dominant_score = joy_score
            dominant_emotion = "joy"
        if dominant_score < sadness_score:
            dominant_emotion = "sadness"
        
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    #Return a dict of the scores and the dominant emotion
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    