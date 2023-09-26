from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('devices.json', 'r') as json_file:
        device_data = json.load(json_file)
    return render_template('index.html', devices=device_data)

if __name__ == '__main__':
    app.run(debug=True)
