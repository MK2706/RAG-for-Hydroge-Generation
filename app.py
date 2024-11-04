from flask import Flask
from flask_ngrok import run_with_ngrok

# Initialize the Flask application
app = Flask(__name__)

# Start Ngrok when the app is run
run_with_ngrok(app)

@app.route('/')
def home():
    return "Hello, World!"  # Response for the root URL

if __name__ == '__main__':
    app.run()  # Run the application
