"""Server for sentiment analyis."""
from flask import Flask, request, make_response
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def hello():
    '''endpoint for sentiment analysis'''
    data = emotion_detector(request.args['textToAnalyze'])
    if data['dominant_emotion'] is None:
        return make_response('Invalid text! Please try again!.\n', 400)
    return (
        "For the given statement, " +
        f"the system response is 'anger': {data['anger']}, " +
        f"'disgust': {data['disgust']}," +
        f"'fear': {data['fear']}, " +
        f"'joy': {data['joy']} " +
        f"and 'sadness': {data['sadness']}. " +
        f"The dominant emotion is {data['dominant_emotion']}."
    )
    