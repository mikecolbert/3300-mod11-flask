# Mike Colbert 04/01/2025

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')  # Render the index.html template when accessing the root URL

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)