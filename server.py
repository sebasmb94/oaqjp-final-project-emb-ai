''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions with their
        different scores and the dominant one.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    text = "For the given statement, the system response is"
    text += f" 'anger': {result['anger']}, 'disgust': {result['disgust']}," 
    text += f" 'fear': {result['fear']}, 'joy': {result['joy']}"
    text += f" and 'sadness': {result['sadness']}." 
    text += f" The dominant emotion is {result['dominant_emotion']}."

    return text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
