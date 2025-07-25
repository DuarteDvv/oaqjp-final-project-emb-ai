"""Flask application for Emotion Detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint that analyzes the provided text for emotions using the emotion_detector function.
    Retrieves text from query parameter 'textToAnalyze' and returns a formatted response string.
    """
    # Retrieve the input text
    text_to_analyze = request.args.get('textToAnalyze')

    # Perform emotion detection
    response = emotion_detector(text_to_analyze)

    if response is None:
        result = "Invalid input! Try again."
    else:
        result = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")

    return result

@app.route("/")
def render_index_page():
    """
    Renders the main index page with the user interface for input.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
