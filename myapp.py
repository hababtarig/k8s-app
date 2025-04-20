from flask import Flask

app = Flask(__name__)

@app.route('/')
def message():
    with open('/app/message.txt') as f:
        return f.read()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
