from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api", methods=['POST'])
def hello():
    result = {
        "results": request.json["text"].split()
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
