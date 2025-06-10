''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initialize the application
app = Flask( "Emotion Detector" )

@app.route("/emotionDetector" )
def detect_emotion():
    '''
    This recieves data from the HTML interface and detects the emotion
    of the provided text via emotion_detector() function.  The output is
    in the form anger, disgust, fear, joy, sadness, and then the dominant
    emotion of the text. 
    '''
    text_to_analyze = request.args.get( 'textToAnalyze' )

    response = emotion_detector( text_to_analyze )

    dominant_emotion = response[ 'dominant_emotion' ]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response[ 'anger' ]
    disgust = response[ 'disgust' ]
    fear = response[ 'fear' ]
    joy = response[ 'joy' ]
    sadness = response[ 'sadness' ]

    return (f"For the given statement, the system response is 'anger': {anger},"
    f"'disgust': {disgust}\n'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."
    f"The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html' )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    