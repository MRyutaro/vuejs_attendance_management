from models import DataBase
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api", methods=['POST'])
def hello():
    db = DataBase()
    text_list = request.json["text"].split()
    print(text_list)
    text = "".join(text_list)
    print("入力された内容--->" + text)
    db.insert(text)
    result_data = db.select()
    result = {
        "results": result_data
    }
    db.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
