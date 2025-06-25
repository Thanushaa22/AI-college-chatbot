from flask import Flask, render_template, request, jsonify
from chatbot_engine import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['POST'])
def chatbot_reply():
    user_input = request.form['msg']
    response = get_response(user_input)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
