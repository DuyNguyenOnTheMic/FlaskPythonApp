from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello bà yêu"

if __name__ == "main":
    app.run(debug=True)