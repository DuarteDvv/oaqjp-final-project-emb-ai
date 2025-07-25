import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):

        q = 'I am glad this happened'
        y = 'joy'

        y_hat = emotion_detector(q)['dominant_emotion']
        self.assertEqual(y_hat,y)

        q = 'I am really mad about this'
        y = 'anger'

        y_hat = emotion_detector(q)['dominant_emotion']
        self.assertEqual(y_hat,y)

        q = 'I feel disgusted just hearing about this'
        y = 'disgust'

        y_hat = emotion_detector(q)['dominant_emotion']
        self.assertEqual(y_hat,y)

        q = 'I am so sad about this'
        y = 'sadness'

        y_hat = emotion_detector(q)['dominant_emotion']
        self.assertEqual(y_hat,y)

        q = 'I am really afraid that this will happen'
        y = 'fear'

        y_hat = emotion_detector(q)['dominant_emotion']
        self.assertEqual(y_hat,y)

        
unittest.main()
