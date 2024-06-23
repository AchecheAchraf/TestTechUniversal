from flask import Flask
from flask_cors import CORS
from api.ocr import ocr_route
from api.text_to_speech import tts_route

app = Flask(__name__)
CORS(app)

app.register_blueprint(ocr_route)
app.register_blueprint(tts_route)

if __name__ == '__main__':
    app.run(debug=True)
