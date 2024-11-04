from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when the app is run

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
